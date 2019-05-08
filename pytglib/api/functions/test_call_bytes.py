

from ..utils import Object


class TestCallBytes(Object):
    """
    Returns the received bytes; for testing only. This is an offline method. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestCallBytes``

    Args:
        x (:obj:`bytes`):
            Bytes to return

    Returns:
        TestBytes

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallBytes"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # bytes

    @staticmethod
    def read(q: dict, *args) -> "TestCallBytes":
        x = q.get('x')
        return TestCallBytes(x)
