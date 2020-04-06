

from ..utils import Object


class SetSupergroupStickerSet(Object):
    """
    Changes the sticker set of a supergroup; requires can_change_info rights 

    Attributes:
        ID (:obj:`str`): ``SetSupergroupStickerSet``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup 
        sticker_set_id (:obj:`int`):
            New value of the supergroup sticker set identifierUse 0 to remove the supergroup sticker set

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setSupergroupStickerSet"

    def __init__(self, supergroup_id, sticker_set_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.sticker_set_id = sticker_set_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SetSupergroupStickerSet":
        supergroup_id = q.get('supergroup_id')
        sticker_set_id = q.get('sticker_set_id')
        return SetSupergroupStickerSet(supergroup_id, sticker_set_id)
