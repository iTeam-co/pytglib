

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
    def read(q: dict, *args) -> "ChatReportReasonCustom or ChatReportReasonPersonalDetails or ChatReportReasonFake or ChatReportReasonViolence or ChatReportReasonChildAbuse or ChatReportReasonIllegalDrugs or ChatReportReasonSpam or ChatReportReasonUnrelatedLocation or ChatReportReasonCopyright or ChatReportReasonPornography":
        if q.get("@type"):
            return Object.read(q)
        return ChatReportReason()
