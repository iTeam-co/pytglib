

from ..utils import Object


class PushMessageContentSticker(Object):
    """
    A message with a sticker 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentSticker``

    Args:
        sticker (:class:`telegram.api.types.sticker`):
            Message content; may be null 
        emoji (:obj:`str`):
            Emoji corresponding to the sticker; may be empty 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentSticker"

    def __init__(self, sticker, emoji, is_pinned, **kwargs):
        
        self.sticker = sticker  # Sticker
        self.emoji = emoji  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentSticker":
        sticker = Object.read(q.get('sticker'))
        emoji = q.get('emoji')
        is_pinned = q.get('is_pinned')
        return PushMessageContentSticker(sticker, emoji, is_pinned)
