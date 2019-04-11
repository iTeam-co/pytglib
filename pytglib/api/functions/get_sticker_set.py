

from ..utils import Object


class GetStickerSet(Object):
    """
    Returns information about a sticker set by its identifier 

    Attributes:
        ID (:obj:`str`): ``GetStickerSet``

    Args:
        set_id (:obj:`int`):
            Identifier of the sticker set

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "getStickerSet"

    def __init__(self, set_id, extra=None, **kwargs):
        self.extra = extra
        self.set_id = set_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetStickerSet":
        set_id = q.get('set_id')
        return GetStickerSet(set_id)
