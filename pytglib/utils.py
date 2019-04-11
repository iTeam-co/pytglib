import time
import uuid
from typing import TYPE_CHECKING, Any, Dict, Optional
from pytglib.api import types, functions
from pytglib.api.utils import *

if TYPE_CHECKING:
    from pytglib.client import Telegram    # noqa  pylint: disable=cyclic-import


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
            #self.update = Error(update["code"], update["message"])
        else:
            self.update = Object.read(update)
