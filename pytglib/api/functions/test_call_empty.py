

from ..utils import Object


class TestCallEmpty(Object):
    """
    Does nothing; for testing only. This is an offline method. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``TestCallEmpty``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "testCallEmpty"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TestCallEmpty":
        
        return TestCallEmpty()
