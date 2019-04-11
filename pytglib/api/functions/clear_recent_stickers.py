

from ..utils import Object


class ClearRecentStickers(Object):
    """
    Clears the list of recently used stickers 

    Attributes:
        ID (:obj:`str`): ``ClearRecentStickers``

    Args:
        is_attached (:obj:`bool`):
            Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "clearRecentStickers"

    def __init__(self, is_attached, extra=None, **kwargs):
        self.extra = extra
        self.is_attached = is_attached  # bool

    @staticmethod
    def read(q: dict, *args) -> "ClearRecentStickers":
        is_attached = q.get('is_attached')
        return ClearRecentStickers(is_attached)
