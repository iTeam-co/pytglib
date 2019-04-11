

from ..utils import Object


class TestVectorStringObject(Object):
    """
    A simple object containing a vector of objects that hold a string; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestVectorStringObject``

    Args:
        value (List of :class:`telegram.api.types.testString`):
            Vector of objects

    Returns:
        TestVectorStringObject

    Raises:
        :class:`telegram.Error`
    """
    ID = "testVectorStringObject"

    def __init__(self, value, **kwargs):
        
        self.value = value  # list of testString

    @staticmethod
    def read(q: dict, *args) -> "TestVectorStringObject":
        value = [Object.read(i) for i in q.get('value', [])]
        return TestVectorStringObject(value)
