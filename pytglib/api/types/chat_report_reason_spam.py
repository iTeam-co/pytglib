

from ..utils import Object


class ChatReportReasonSpam(Object):
    """
    The chat contains spam messages

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonSpam``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonSpam"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonSpam":
        
        return ChatReportReasonSpam()
