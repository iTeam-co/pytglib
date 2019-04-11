

from ..utils import Object


class UpdateInstalledStickerSets(Object):
    """
    The list of installed sticker sets was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateInstalledStickerSets``

    Args:
        is_masks (:obj:`bool`):
            True, if the list of installed mask sticker sets was updated 
        sticker_set_ids (List of :obj:`int`):
            The new list of installed ordinary sticker sets

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateInstalledStickerSets"

    def __init__(self, is_masks, sticker_set_ids, **kwargs):
        
        self.is_masks = is_masks  # bool
        self.sticker_set_ids = sticker_set_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateInstalledStickerSets":
        is_masks = q.get('is_masks')
        sticker_set_ids = q.get('sticker_set_ids')
        return UpdateInstalledStickerSets(is_masks, sticker_set_ids)
