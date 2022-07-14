

from ..utils import Object


class ChatReportReasonIllegalDrugs(Object):
    """
    The chat has illegal drugs related content

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonIllegalDrugs``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonIllegalDrugs"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonIllegalDrugs":
        
        return ChatReportReasonIllegalDrugs()
