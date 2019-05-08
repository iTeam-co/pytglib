

from ..utils import Object


class ChatReportReasonChildAbuse(Object):
    """
    The chat has child abuse related content

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonChildAbuse``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonChildAbuse"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonChildAbuse":
        
        return ChatReportReasonChildAbuse()
