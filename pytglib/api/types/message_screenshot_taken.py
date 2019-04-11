

from ..utils import Object


class MessageScreenshotTaken(Object):
    """
    A screenshot of a message in the chat has been taken

    Attributes:
        ID (:obj:`str`): ``MessageScreenshotTaken``

    No parameters required.

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageScreenshotTaken"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "MessageScreenshotTaken":
        
        return MessageScreenshotTaken()
