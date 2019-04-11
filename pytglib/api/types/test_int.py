

from ..utils import Object


class TestInt(Object):
    """
    A simple object containing a number; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestInt``

    Args:
        value (:obj:`int`):
            Number

    Returns:
        TestInt

    Raises:
        :class:`telegram.Error`
    """
    ID = "testInt"

    def __init__(self, value, **kwargs):
        
        self.value = value  # int

    @staticmethod
    def read(q: dict, *args) -> "TestInt":
        value = q.get('value')
        return TestInt(value)
