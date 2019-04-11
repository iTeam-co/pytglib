

from ..utils import Object


class ReorderInstalledStickerSets(Object):
    """
    Changes the order of installed sticker sets 

    Attributes:
        ID (:obj:`str`): ``ReorderInstalledStickerSets``

    Args:
        is_masks (:obj:`bool`):
            Pass true to change the order of mask sticker sets; pass false to change the order of ordinary sticker sets 
        sticker_set_ids (List of :obj:`int`):
            Identifiers of installed sticker sets in the new correct order

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reorderInstalledStickerSets"

    def __init__(self, is_masks, sticker_set_ids, extra=None, **kwargs):
        self.extra = extra
        self.is_masks = is_masks  # bool
        self.sticker_set_ids = sticker_set_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ReorderInstalledStickerSets":
        is_masks = q.get('is_masks')
        sticker_set_ids = q.get('sticker_set_ids')
        return ReorderInstalledStickerSets(is_masks, sticker_set_ids)
