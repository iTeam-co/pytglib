

from ..utils import Object


class TestCallString(Object):
    """
    Returns the received string; for testing only. This is an offline method. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestCallString``

    Args:
        x (:obj:`str`):
            String to return

    Returns:
        TestString

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallString"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # str

    @staticmethod
    def read(q: dict, *args) -> "TestCallString":
        x = q.get('x')
        return TestCallString(x)
