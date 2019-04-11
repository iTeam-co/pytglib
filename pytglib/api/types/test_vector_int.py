

from ..utils import Object


class TestVectorInt(Object):
    """
    A simple object containing a vector of numbers; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestVectorInt``

    Args:
        value (List of :obj:`int`):
            Vector of numbers

    Returns:
        TestVectorInt

    Raises:
        :class:`telegram.Error`
    """
    ID = "testVectorInt"

    def __init__(self, value, **kwargs):
        
        self.value = value  # list of int

    @staticmethod
    def read(q: dict, *args) -> "TestVectorInt":
        value = q.get('value')
        return TestVectorInt(value)
