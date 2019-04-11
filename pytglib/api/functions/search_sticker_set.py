

from ..utils import Object


class SearchStickerSet(Object):
    """
    Searches for a sticker set by its name 

    Attributes:
        ID (:obj:`str`): ``SearchStickerSet``

    Args:
        name (:obj:`str`):
            Name of the sticker set

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchStickerSet"

    def __init__(self, name, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchStickerSet":
        name = q.get('name')
        return SearchStickerSet(name)
