

from ..utils import Object


class ChatReportReasonCopyright(Object):
    """
    The chat contains copyrighted content

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonCopyright``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonCopyright"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonCopyright":
        
        return ChatReportReasonCopyright()
