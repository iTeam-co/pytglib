

from ..utils import Object


class PushMessageContentScreenshotTaken(Object):
    """
    A screenshot of a message in the chat has been taken

    Attributes:
        ID (:obj:`str`): ``PushMessageContentScreenshotTaken``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentScreenshotTaken"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentScreenshotTaken":
        
        return PushMessageContentScreenshotTaken()
