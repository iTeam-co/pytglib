

from ..utils import Object


class ChatReportReasonPornography(Object):
    """
    The chat contains pornographic messages

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonPornography``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonPornography"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonPornography":
        
        return ChatReportReasonPornography()
