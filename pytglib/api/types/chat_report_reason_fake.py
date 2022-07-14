

from ..utils import Object


class ChatReportReasonFake(Object):
    """
    The chat represents a fake account

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonFake``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonFake"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonFake":
        
        return ChatReportReasonFake()
