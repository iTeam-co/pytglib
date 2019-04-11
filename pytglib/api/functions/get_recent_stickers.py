

from ..utils import Object


class GetRecentStickers(Object):
    """
    Returns a list of recently used stickers 

    Attributes:
        ID (:obj:`str`): ``GetRecentStickers``

    Args:
        is_attached (:obj:`bool`):
            Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers

    Returns:
        Stickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecentStickers"

    def __init__(self, is_attached, extra=None, **kwargs):
        self.extra = extra
        self.is_attached = is_attached  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetRecentStickers":
        is_attached = q.get('is_attached')
        return GetRecentStickers(is_attached)
