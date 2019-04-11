

from ..utils import Object


class UpdateRecentStickers(Object):
    """
    The list of recently used stickers was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateRecentStickers``

    Args:
        is_attached (:obj:`bool`):
            True, if the list of stickers attached to photo or video files was updated, otherwise the list of sent stickers is updated 
        sticker_ids (List of :obj:`int`):
            The new list of file identifiers of recently used stickers

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateRecentStickers"

    def __init__(self, is_attached, sticker_ids, **kwargs):
        
        self.is_attached = is_attached  # bool
        self.sticker_ids = sticker_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateRecentStickers":
        is_attached = q.get('is_attached')
        sticker_ids = q.get('sticker_ids')
        return UpdateRecentStickers(is_attached, sticker_ids)
