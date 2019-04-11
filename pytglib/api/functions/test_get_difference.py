

from ..utils import Object


class TestGetDifference(Object):
    """
    Forces an updates.getDifference call to the Telegram servers; for testing only

    Attributes:
        ID (:obj:`str`): ``TestGetDifference``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "testGetDifference"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TestGetDifference":
        
        return TestGetDifference()
