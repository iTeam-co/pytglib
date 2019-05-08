

from ..utils import Object


class TestCallVectorInt(Object):
    """
    Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestCallVectorInt``

    Args:
        x (List of :obj:`int`):
            Vector of numbers to return

    Returns:
        TestVectorInt

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallVectorInt"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # list of int

    @staticmethod
    def read(q: dict, *args) -> "TestCallVectorInt":
        x = q.get('x')
        return TestCallVectorInt(x)
