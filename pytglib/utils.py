import time
import uuid
from typing import TYPE_CHECKING, Any, Dict, Optional
import threading
from pytglib.api import types, functions
from pytglib.api.utils import *

if TYPE_CHECKING:
    from pytglib.client import Telegram  # noqa  pylint: disable=cyclic-import


class AsyncResult:
    """
    tdlib is asynchronous, and this class helps you get results back.
    After each API call, you receive AsyncResult object, which you can use to get results back.
    """

    def __init__(self, client: 'Telegram', result_id=None) -> None:
        self.client = client

        if result_id:
            self.id = result_id
        else:
            self.id = uuid.uuid4().hex

        self.request: Optional[Dict[Any, Any]] = None
        self.error = False
        self.update: Object = None

    def __str__(self):
        return f'AsyncResult <{self.id}>'

    def wait(self, timeout: int = None, raise_exc: bool = False) -> None:
        """
        Blocking method to wait for the result
        """
        started_at = time.time()
        while True:
            if self.update or self.error:
                if raise_exc and self.error:
                    raise self.error_info
                return
            time.sleep(0.01)
            if timeout and time.time() - started_at > timeout:
                raise TimeoutError()

    def parse_update(self, update: dict) -> None:
        if update.get('@type') == 'ok':
            self.update = types.Ok()
        elif update.get('@type') == 'error':
            self.error = True
            self.error_info = update
            self.update = False
            # self.update = Error(update["code"], update["message"])
        else:
            self.update = Object.read(update)


class Promise(object):
    """A simple Promise implementation for use with the run_async decorator, DelayQueue etc.
    Args:
        pooled_function (:obj:`callable`): The callable that will be called concurrently.
        args (:obj:`list` | :obj:`tuple`): Positional arguments for :attr:`pooled_function`.
        kwargs (:obj:`dict`): Keyword arguments for :attr:`pooled_function`.
    Attributes:
        pooled_function (:obj:`callable`): The callable that will be called concurrently.
        args (:obj:`list` | :obj:`tuple`): Positional arguments for :attr:`pooled_function`.
        kwargs (:obj:`dict`): Keyword arguments for :attr:`pooled_function`.
        done (:obj:`threading.Event`): Is set when the result is available.
    """

    def __init__(self, pooled_function, args, kwargs, logger=None):
        self.pooled_function = pooled_function
        self.args = args
        self.kwargs = kwargs
        self.done = threading.Event()
        self._result = None
        self._exception = None
        self.logger = logger

    def run(self):
        """Calls the :attr:`pooled_function` callable."""

        try:
            self._result = self.pooled_function(*self.args, **self.kwargs)

        except Exception as exc:
            self._exception = exc

        finally:
            self.done.set()

    def __call__(self):
        self.run()

    def result(self, timeout=None):
        """Return the result of the ``Promise``.
        Args:
            timeout (:obj:`float`, optional): Maximum time in seconds to wait for the result to be
                calculated. ``None`` means indefinite. Default is ``None``.
        Returns:
            Returns the return value of :attr:`pooled_function` or ``None`` if the ``timeout``
            expires.
        Raises:
            Any exception raised by :attr:`pooled_function`.
        """
        self.done.wait(timeout=timeout)
        if self._exception is not None:
            if self.logger:
                self.logger.exception(f'An uncaught error was raised while running the promise: {self._exception}')
            raise self._exception  # pylint: disable=raising-bad-type
        return self._result

    @property
    def exception(self):
        """The exception raised by :attr:`pooled_function` or ``None`` if no exception has been
        raised (yet)."""
        return self._exception
