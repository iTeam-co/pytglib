

from ..utils import Object


class MessageSticker(Object):
    """
    A sticker message 

    Attributes:
        ID (:obj:`str`): ``MessageSticker``

    Args:
        sticker (:class:`telegram.api.types.sticker`):
            The sticker description 
        is_premium (:obj:`bool`):
            True, if premium animation of the sticker must be played

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSticker"

    def __init__(self, sticker, is_premium, **kwargs):
        
        self.sticker = sticker  # Sticker
        self.is_premium = is_premium  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageSticker":
        sticker = Object.read(q.get('sticker'))
        is_premium = q.get('is_premium')
        return MessageSticker(sticker, is_premium)
