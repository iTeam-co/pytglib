

from ..utils import Object


class TestNetwork(Object):
    """
    Sends a simple network request to the Telegram servers; for testing only

    Attributes:
        ID (:obj:`str`): ``TestNetwork``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "testNetwork"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "TestNetwork":
        
        return TestNetwork()
