

from ..utils import Object


class RemoveRecentSticker(Object):
    """
    Removes a sticker from the list of recently used stickers 

    Attributes:
        ID (:obj:`str`): ``RemoveRecentSticker``

    Args:
        is_attached (:obj:`bool`):
            Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers 
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker file to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeRecentSticker"

    def __init__(self, is_attached, sticker, extra=None, **kwargs):
        self.extra = extra
        self.is_attached = is_attached  # bool
        self.sticker = sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "RemoveRecentSticker":
        is_attached = q.get('is_attached')
        sticker = Object.read(q.get('sticker'))
        return RemoveRecentSticker(is_attached, sticker)
