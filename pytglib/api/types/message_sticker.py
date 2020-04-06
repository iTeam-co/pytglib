

from ..utils import Object


class MessageSticker(Object):
    """
    A sticker message 

    Attributes:
        ID (:obj:`str`): ``MessageSticker``

    Args:
        sticker (:class:`telegram.api.types.sticker`):
            The sticker description

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSticker"

    def __init__(self, sticker, **kwargs):
        
        self.sticker = sticker  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "MessageSticker":
        sticker = Object.read(q.get('sticker'))
        return MessageSticker(sticker)
