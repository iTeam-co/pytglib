

from ..utils import Object


class TestVectorString(Object):
    """
    A simple object containing a vector of strings; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestVectorString``

    Args:
        value (List of :obj:`str`):
            Vector of strings

    Returns:
        TestVectorString

    Raises:
        :class:`telegram.Error`
    """
    ID = "testVectorString"

    def __init__(self, value, **kwargs):
        
        self.value = value  # list of str

    @staticmethod
    def read(q: dict, *args) -> "TestVectorString":
        value = q.get('value')
        return TestVectorString(value)
