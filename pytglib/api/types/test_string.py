

from ..utils import Object


class TestString(Object):
    """
    A simple object containing a string; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestString``

    Args:
        value (:obj:`str`):
            String

    Returns:
        TestString

    Raises:
        :class:`telegram.Error`
    """
    ID = "testString"

    def __init__(self, value, **kwargs):
        
        self.value = value  # str

    @staticmethod
    def read(q: dict, *args) -> "TestString":
        value = q.get('value')
        return TestString(value)
