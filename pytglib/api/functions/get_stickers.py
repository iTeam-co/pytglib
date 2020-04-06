

from ..utils import Object


class GetStickers(Object):
    """
    Returns stickers from the installed sticker sets that correspond to a given emoji. If the emoji is not empty, favorite and recently used stickers may also be returned 

    Attributes:
        ID (:obj:`str`): ``GetStickers``

    Args:
        emoji (:obj:`str`):
            String representation of emojiIf empty, returns all known installed stickers 
        limit (:obj:`int`):
            The maximum number of stickers to be returned

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStickers"

    def __init__(self, emoji, limit, extra=None, **kwargs):
        self.extra = extra
        self.emoji = emoji  # str
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetStickers":
        emoji = q.get('emoji')
        limit = q.get('limit')
        return GetStickers(emoji, limit)
