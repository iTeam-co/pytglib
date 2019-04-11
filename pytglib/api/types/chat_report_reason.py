

from ..utils import Object


class ChatReportReason(Object):
    """
    Describes the reason why a chat is reported

    No parameters required.
    """
    ID = "chatReportReason"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonCustom or ChatReportReasonPornography or ChatReportReasonViolence or ChatReportReasonCopyright or ChatReportReasonSpam":
        if q.get("@type"):
            return Object.read(q)
        return ChatReportReason()
