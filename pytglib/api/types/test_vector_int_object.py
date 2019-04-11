

from ..utils import Object


class TestVectorIntObject(Object):
    """
    A simple object containing a vector of objects that hold a number; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestVectorIntObject``

    Args:
        value (List of :class:`telegram.api.types.testInt`):
            Vector of objects

    Returns:
        TestVectorIntObject

    Raises:
        :class:`telegram.Error`
    """
    ID = "testVectorIntObject"

    def __init__(self, value, **kwargs):
        
        self.value = value  # list of testInt

    @staticmethod
    def read(q: dict, *args) -> "TestVectorIntObject":
        value = [Object.read(i) for i in q.get('value', [])]
        return TestVectorIntObject(value)
