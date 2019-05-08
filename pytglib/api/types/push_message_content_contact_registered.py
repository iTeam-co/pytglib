

from ..utils import Object


class PushMessageContentContactRegistered(Object):
    """
    A contact has registered with Telegram

    Attributes:
        ID (:obj:`str`): ``PushMessageContentContactRegistered``

    No parameters required.

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentContactRegistered"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentContactRegistered":
        
        return PushMessageContentContactRegistered()
