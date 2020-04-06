

from ..utils import Object


class ChatActionBarReportSpam(Object):
    """
    The chat can be reported as spam using the method reportChat with the reason chatReportReasonSpam

    Attributes:
        ID (:obj:`str`): ``ChatActionBarReportSpam``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarReportSpam"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarReportSpam":
        
        return ChatActionBarReportSpam()
