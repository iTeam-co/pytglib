

from ..utils import Object


class ChatReportReasonPersonalDetails(Object):
    """
    The chat contains messages with personal details

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonPersonalDetails``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonPersonalDetails"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonPersonalDetails":
        
        return ChatReportReasonPersonalDetails()
