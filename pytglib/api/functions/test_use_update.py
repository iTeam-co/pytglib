

from ..utils import Object


class TestUseUpdate(Object):
    """
    Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``TestUseUpdate``

    No parameters required.

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "testUseUpdate"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TestUseUpdate":
        
        return TestUseUpdate()
