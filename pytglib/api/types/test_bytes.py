

from ..utils import Object


class TestBytes(Object):
    """
    A simple object containing a sequence of bytes; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestBytes``

    Args:
        value (:obj:`bytes`):
            Bytes

    Returns:
        TestBytes

    Raises:
        :class:`telegram.Error`
    """
    ID = "testBytes"

    def __init__(self, value, **kwargs):
        
        self.value = value  # bytes

    @staticmethod
    def read(q: dict, *args) -> "TestBytes":
        value = q.get('value')
        return TestBytes(value)
