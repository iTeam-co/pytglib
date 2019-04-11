

from ..utils import Object


class ChatActionChoosingLocation(Object):
    """
    The user is picking a location or venue to send

    Attributes:
        ID (:obj:`str`): ``ChatActionChoosingLocation``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionChoosingLocation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionChoosingLocation":
        
        return ChatActionChoosingLocation()
