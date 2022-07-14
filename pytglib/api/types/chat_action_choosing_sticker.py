

from ..utils import Object


class ChatActionChoosingSticker(Object):
    """
    The user is picking a sticker to send

    Attributes:
        ID (:obj:`str`): ``ChatActionChoosingSticker``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionChoosingSticker"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionChoosingSticker":
        
        return ChatActionChoosingSticker()
