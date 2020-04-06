import logging
import threading
from queue import Queue
from pytglib.api.utils import Object
from .utils import Promise

logger = logging.getLogger(__name__)


class BaseWorker:
    """
    Base worker class.
    Each worker must implement the run method to start listening to the queue
    and calling handler functions
    """

    def __init__(self, queue: Queue) -> None:
        self._is_enabled = True
        self._queue = queue

    def run(self) -> None:
        raise NotImplementedError()


class SimpleWorker(BaseWorker):
    """Simple one-thread worker"""

    def run(self) -> None:
        self._thread = threading.Thread(target=self._run_thread)  # pylint: disable=attribute-defined-outside-init
        self._thread.daemon = True
        self._thread.start()

    def _run_thread(self) -> None:
        logger.info('[SimpleWorker] started')

        while self._is_enabled:
            handler, update = self._queue.get()
            handler(Object.read(update))
            self._queue.task_done()


class ThreadedWorker(BaseWorker):
    """
    Simple multi-thread worker
    """

    def run(self) -> None:
        self._thread = threading.Thread(target=self._run_thread)  # pylint: disable=attribute-defined-outside-init
        self._thread.daemon = True
        self._thread.start()

    def _run_thread(self) -> None:
        logger.info('[SimpleWorker] started')

        while self._is_enabled:
            handler, update = self._queue.get()
            promise = Promise(handler, (Object.read(update)), {}, logger)
            threading.Thread(target=promise.run).start()
            self._queue.task_done()
