

from ..utils import Object


class TestUseError(Object):
    """
    Does nothing and ensures that the Error object is used; for testing only. This is an offline method. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``TestUseError``

    No parameters required.

    Returns:
        Error

    Raises:
        :class:`telegram.Error`
    """
    ID = "testUseError"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TestUseError":
        
        return TestUseError()
