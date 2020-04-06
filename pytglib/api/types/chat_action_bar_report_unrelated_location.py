

from ..utils import Object


class ChatActionBarReportUnrelatedLocation(Object):
    """
    The chat is a location-based supergroup, which can be reported as having unrelated location using the method reportChat with the reason chatReportReasonUnrelatedLocation

    Attributes:
        ID (:obj:`str`): ``ChatActionBarReportUnrelatedLocation``

    No parameters required.

    Returns:
        ChatActionBar

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionBarReportUnrelatedLocation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionBarReportUnrelatedLocation":
        
        return ChatActionBarReportUnrelatedLocation()
