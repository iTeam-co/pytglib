

from ..utils import Object


class TestCallVectorString(Object):
    """
    For testing only request. Returns the received vector of strings; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestCallVectorString``

    Args:
        x (List of :obj:`str`):
            Vector of strings to return

    Returns:
        TestVectorString

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallVectorString"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # list of str

    @staticmethod
    def read(q: dict, *args) -> "TestCallVectorString":
        x = q.get('x')
        return TestCallVectorString(x)
