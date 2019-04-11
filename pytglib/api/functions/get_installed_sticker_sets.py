

from ..utils import Object


class GetInstalledStickerSets(Object):
    """
    Returns a list of installed sticker sets 

    Attributes:
        ID (:obj:`str`): ``GetInstalledStickerSets``

    Args:
        is_masks (:obj:`bool`):
            Pass true to return mask sticker sets; pass false to return ordinary sticker sets

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInstalledStickerSets"

    def __init__(self, is_masks, extra=None, **kwargs):
        self.extra = extra
        self.is_masks = is_masks  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetInstalledStickerSets":
        is_masks = q.get('is_masks')
        return GetInstalledStickerSets(is_masks)
