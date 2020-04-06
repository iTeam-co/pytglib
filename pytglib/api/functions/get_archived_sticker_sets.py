

from ..utils import Object


class GetArchivedStickerSets(Object):
    """
    Returns a list of archived sticker sets 

    Attributes:
        ID (:obj:`str`): ``GetArchivedStickerSets``

    Args:
        is_masks (:obj:`bool`):
            Pass true to return mask stickers sets; pass false to return ordinary sticker sets 
        offset_sticker_set_id (:obj:`int`):
            Identifier of the sticker set from which to return the result 
        limit (:obj:`int`):
            The maximum number of sticker sets to return

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getArchivedStickerSets"

    def __init__(self, is_masks, offset_sticker_set_id, limit, extra=None, **kwargs):
        self.extra = extra
        self.is_masks = is_masks  # bool
        self.offset_sticker_set_id = offset_sticker_set_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetArchivedStickerSets":
        is_masks = q.get('is_masks')
        offset_sticker_set_id = q.get('offset_sticker_set_id')
        limit = q.get('limit')
        return GetArchivedStickerSets(is_masks, offset_sticker_set_id, limit)
