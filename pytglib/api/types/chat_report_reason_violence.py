

from ..utils import Object


class ChatReportReasonViolence(Object):
    """
    The chat promotes violence

    Attributes:
        ID (:obj:`str`): ``ChatReportReasonViolence``

    No parameters required.

    Returns:
        ChatReportReason

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatReportReasonViolence"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatReportReasonViolence":
        
        return ChatReportReasonViolence()
