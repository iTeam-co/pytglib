

from ..utils import Object


class TestCallVectorIntObject(Object):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``TestCallVectorIntObject``

    Args:
        x (List of :class:`telegram.api.types.testInt`):
            Vector of objects to return

    Returns:
        TestVectorIntObject

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallVectorIntObject"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # list of testInt

    @staticmethod
    def read(q: dict, *args) -> "TestCallVectorIntObject":
        x = [Object.read(i) for i in q.get('x', [])]
        return TestCallVectorIntObject(x)
