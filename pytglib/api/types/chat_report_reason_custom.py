

from ..utils import Object


class ChatReportReasonCustom(Object):
    """
    A custom reason provided by the user

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonCustom``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonCustom"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonCustom":
        
        return ChatReportReasonCustom()
