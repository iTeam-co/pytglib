

from ..utils import Object


class InternalLinkTypeStickerSet(Object):
    """
    The link is a link to a sticker set. Call searchStickerSet with the given sticker set name to process the link and show the sticker set 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeStickerSet``

    Args:
        sticker_set_name (:obj:`str`):
            Name of the sticker set

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeStickerSet"

    def __init__(self, sticker_set_name, **kwargs):
        
        self.sticker_set_name = sticker_set_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeStickerSet":
        sticker_set_name = q.get('sticker_set_name')
        return InternalLinkTypeStickerSet(sticker_set_name)
