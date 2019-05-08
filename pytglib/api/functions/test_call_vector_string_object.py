

from ..utils import Object


class TestCallVectorStringObject(Object):
    """
    Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestCallVectorStringObject``

    Args:
        x (List of :class:`telegram.api.types.testString`):
            Vector of objects to return

    Returns:
        TestVectorStringObject

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallVectorStringObject"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # list of testString

    @staticmethod
    def read(q: dict, *args) -> "TestCallVectorStringObject":
        x = [Object.read(i) for i in q.get('x', [])]
        return TestCallVectorStringObject(x)
