import os
import time
import queue
import signal
import typing
import getpass
import logging
import threading
import json
from typing import Any, Dict, List, Type, Callable, Optional, DefaultDict
from collections import defaultdict

from pytglib import VERSION
from pytglib.utils import AsyncResult
from pytglib.tdjson import TDJson
from pytglib.worker import BaseWorker, SimpleWorker
from pytglib.api import Object
from pytglib.functions import Function

logger = logging.getLogger(__name__)

MESSAGE_HANDLER_TYPE: str = 'updateNewMessage'
RAW_UPDATE_HANDLER_TYPE: str = 'update'
DELETE_MESSAGES_HANDLER_TYPE: str = 'updateDeleteMessages'


class Telegram:
    def __init__(
            self,
            library_path,
            api_id: int,
            api_hash: str,
            database_encryption_key: str,
            phone: str = None,
            bot_token: str = None,
            worker: Optional[Type[BaseWorker]] = None,
            files_directory: str = None,
            use_test_dc: bool = False,
            use_message_database: bool = True,
            device_model: str = 'python-telegram',
            application_version: str = VERSION,
            system_version: str = 'unknown',
            system_language_code: str = 'en',
            login: bool = False,
            default_workers_queue_size=1000,
            tdlib_verbosity: int = 2,
    ) -> None:
        """
        Args:
            api_id - ID of your app (https://my.pytglib.org/apps/)
            api_hash - api_hash of your app (https://my.pytglib.org/apps/)
            phone - your phone number
            library_path - you can change path to the compiled libtdjson library
            worker - worker to process updates
            files_directory - directory for the tdlib's files (database, images, etc.)
            use_test_dc - use test datacenter
            use_message_database
            device_model
            application_version
            system_version
            system_language_code
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.library_path = library_path
        self.phone = phone
        self.bot_token = bot_token
        self.use_test_dc = use_test_dc
        self.device_model = device_model
        self.system_version = system_version
        self.system_language_code = system_language_code
        self.application_version = application_version
        self.use_message_database = use_message_database
        self._queue_put_timeout = 10

        if not self.bot_token and not self.phone:
            raise ValueError('You must provide bot_token or phone')

        self._database_encryption_key = database_encryption_key

        if not files_directory:
            files_directory = f'/tmp/.tdlib_files/{self.phone}/'
        self.files_directory = files_directory

        self._authorized = False
        self._is_enabled = False

        # todo: move to worker
        self._workers_queue: queue.Queue = queue.Queue(
            maxsize=default_workers_queue_size
        )

        if not worker:
            worker = SimpleWorker
        self.worker = worker(queue=self._workers_queue)

        self._results: Dict[str, AsyncResult] = {}
        self._update_handlers: DefaultDict[str, List[Callable]] = defaultdict(list)

        self._tdjson = TDJson(library_path=library_path, verbosity=tdlib_verbosity)
        self._run()

        self.functions = Function(self)

        if login:
            self.login()

    def __del__(self):
        self.stop()

    def stop(self) -> None:
        """Stops the client"""
        self._is_enabled = False

        if hasattr(self, '_tdjson'):
            self._tdjson.stop()

    def call_method(self, method_name: str, params: Optional[Dict[str, Any]] = None):
        data = {'@type': method_name}

        if params:
            data.update(params)

        return self._send_data(data)

    def _run(self):
        self._is_enabled = True

        self._td_listener = threading.Thread(target=self._listen_to_td)
        self._td_listener.daemon = True
        self._td_listener.start()

        self.worker.run()

    def _listen_to_td(self):
        logger.info('[pytglib.td_listener] started')

        while self._is_enabled:
            update = self._tdjson.receive()

            if update:
                self._update_async_result(update)
                self._run_handlers(update)

    def _update_async_result(self, update: dict) -> typing.Optional[AsyncResult]:
        async_result = None

        _special_types = (
            'updateAuthorizationState',
        )  # for authorizationProcess @extra.request_id doesn't work

        if update.get('@type') in _special_types:
            request_id = update['@type']
        else:
            request_id = update.get('@extra', {}).get('request_id')

        if not request_id:
            logger.debug('request_id has not been found in the update')
        else:
            async_result = self._results.get(request_id)

        if not async_result:
            logger.debug(
                'async_result has not been found in by request_id=%s', request_id
            )
        else:
            async_result.parse_update(update)
            self._results.pop(request_id, None)

        return async_result

    def _run_handlers(self, update: Dict[Any, Any]) -> None:
        update_type: str = update.get('@type', 'unknown')
        for handler in self._update_handlers[update_type]:
            self._workers_queue.put((handler, update), timeout=self._queue_put_timeout)
        for handler in self._update_handlers[RAW_UPDATE_HANDLER_TYPE]:
            self._workers_queue.put((handler, update), timeout=self._queue_put_timeout)

    def add_message_handler(self, func: Callable) -> None:
        """
        Adds function to handle all incoming messages
        Args:
            func (:obj:`Callable`):
                Message handler function
        """
        self.add_update_handler(MESSAGE_HANDLER_TYPE, func)

    def add_raw_update_handler(self, func: Callable) -> None:
        """
        Adds function to handle all incoming updates
        Args:
            func (:obj:`Callable`):
                Update handler function
        """
        self.add_update_handler(RAW_UPDATE_HANDLER_TYPE, func)

    def add_delete_messages_handler(self, func: Callable) -> None:
        """
        Adds function to handle deleted messages
        Args:
            func (:obj:`Callable`):
                Deleted messages handler function
        """
        self.add_update_handler(DELETE_MESSAGES_HANDLER_TYPE, func)

    def add_update_handler(self, handler_type: str, func: Callable) -> None:
        """
        Adds function to handle custom type of updates
        Args:
            handler_type (:obj:`str`):
                Update type name
                For example updateNewMessage
            func (:obj:`Callable`):
                Handler function
        """
        if func not in self._update_handlers[handler_type]:
            self._update_handlers[handler_type].append(func)

    def _send_data(self, data: dict, result_id: str = None) -> AsyncResult:
        if '@extra' not in data:
            data['@extra'] = {}

        if not result_id and 'request_id' in data['@extra']:
            result_id = data['@extra']['request_id']

        async_result = AsyncResult(client=self, result_id=result_id)
        data['@extra']['request_id'] = async_result.id

        self._tdjson.send(data)
        self._results[async_result.id] = async_result
        async_result.request = data

        return async_result

    def send(self, data: Object, result_id: str = None) -> AsyncResult:
        data = json.loads(str(data))
        if '@extra' not in data:
            data['@extra'] = {}

        if not result_id and 'request_id' in data['@extra']:
            result_id = data['@extra']['request_id']

        async_result = AsyncResult(client=self, result_id=result_id)
        data['@extra']['request_id'] = async_result.id

        self._tdjson.send(data)
        self._results[async_result.id] = async_result
        async_result.request = data

        return async_result

    def execute(self, data: Object) -> Object:
        data = json.loads(str(data))
        result = self._tdjson.td_execute(data)
        return Object.read(result)

    def idle(self, stop_signals=(signal.SIGINT, signal.SIGTERM, signal.SIGABRT)):
        """Blocks until one of the signals are received and stops"""

        #        for sig in stop_signals:
        #            signal.signal(sig, self._signal_handler)

        self._is_enabled = True

        while self._is_enabled:
            time.sleep(0.1)

    def _signal_handler(self, signum, frame):
        self._is_enabled = False

    def login(self):
        """
        Login process (blocking)

        Must be called before any other call. It sends initial params to the tdlib, sets database encryption key, etc.
        """
        authorization_state = None
        actions = {
            None: self._send_encryption_key,
            'authorizationStateWaitTdlibParameters': self._set_initial_params,
            'authorizationStateWaitEncryptionKey': self._send_encryption_key,
            'authorizationStateWaitPhoneNumber': self._send_phone_number_or_bot_token,
            'authorizationStateWaitCode': self._send_telegram_code,
            'authorizationStateWaitPassword': self._send_password,
            'authorizationStateReady': self._complete_authorization,
        }
        if self.phone:
            logger.info('[login] Login process has been started with phone')
        else:
            logger.info('[login] Login process has been started with bot token')

        while not self._authorized:
            logger.info('[login] current authorization state: %s', authorization_state)
            result = actions[authorization_state]()

            if result:
                result.wait(raise_exc=False)
                res = result.update
                if not res:
                    # print(result.error_info)
                    if result.error_info['message'] == 'Database encryption key is needed:' \
                                                       ' call checkDatabaseEncryptionKey first':
                        authorization_state = 'authorizationStateWaitEncryptionKey'
                    elif result.error_info['message'] == 'Initialization parameters are needed:' \
                                                         ' call setTdlibParameters first':
                        authorization_state = 'authorizationStateWaitTdlibParameters'
                    else:
                        raise ValueError(str(result.error_info))  # TODO: Change to "Error" object
                else:
                    authorization_state = res.authorization_state.ID

    def _set_initial_params(self) -> AsyncResult:
        logger.info(
            'Setting tdlib initial params: files_dir=%s, test_dc=%s',
            self.files_directory,
            self.use_test_dc,
        )
        data = {
            # todo: params
            '@type': 'setTdlibParameters',
            'parameters': {
                'use_test_dc': self.use_test_dc,
                'api_id': self.api_id,
                'api_hash': self.api_hash,
                'device_model': self.device_model,
                'system_version': self.system_version,
                'application_version': self.application_version,
                'system_language_code': self.system_language_code,
                'database_directory': os.path.join(self.files_directory, 'database'),
                'use_message_database': self.use_message_database,
                'files_directory': os.path.join(self.files_directory, 'files'),
            },
        }

        return self._send_data(data, result_id='updateAuthorizationState')

    def _send_encryption_key(self) -> AsyncResult:
        logger.info('Sending encryption key')
        data = {
            '@type': 'checkDatabaseEncryptionKey',
            'encryption_key': self._database_encryption_key,
        }

        return self._send_data(data, result_id='updateAuthorizationState')

    def _send_phone_number_or_bot_token(self) -> AsyncResult:
        """Sends phone number or a bot_token"""
        if self.phone:
            return self._send_phone_number()
        elif self.bot_token:
            return self._send_bot_token()
        else:
            raise RuntimeError('Unknown mode: both bot_token and phone are None')

    def _send_phone_number(self) -> AsyncResult:
        logger.info('Sending phone number')
        data = {
            '@type': 'setAuthenticationPhoneNumber',
            'phone_number': self.phone,
            'allow_flash_call': False,
            'is_current_phone_number': True,
        }

        return self._send_data(data, result_id='updateAuthorizationState')

    def _send_bot_token(self) -> AsyncResult:
        logger.info('Sending bot token')
        data = {'@type': 'checkAuthenticationBotToken', 'token': self.bot_token}

        return self._send_data(data, result_id='updateAuthorizationState')

    def _send_telegram_code(self) -> AsyncResult:
        logger.info('Sending code')
        code = input('Enter code:')
        data = {'@type': 'checkAuthenticationCode', 'code': str(code)}

        return self._send_data(data, result_id='updateAuthorizationState')

    def _send_password(self) -> AsyncResult:
        logger.info('Sending password')
        password = getpass.getpass('Password:')
        data = {'@type': 'checkAuthenticationPassword', 'password': password}

        return self._send_data(data, result_id='updateAuthorizationState')

    def _complete_authorization(self) -> None:
        logger.info('Completing auth process')
        self._authorized = True
