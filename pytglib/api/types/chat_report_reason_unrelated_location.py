

from ..utils import Object


class ChatReportReasonUnrelatedLocation(Object):
    """
    The location-based chat is unrelated to its stated location

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonUnrelatedLocation``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonUnrelatedLocation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonUnrelatedLocation":
        
        return ChatReportReasonUnrelatedLocation()
