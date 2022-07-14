

from ..utils import Object


class GetSuggestedStickerSetName(Object):
    """
    Returns a suggested name for a new sticker set with a given title 

    Attributes:
        ID (:obj:`str`): ``GetSuggestedStickerSetName``

    Args:
        title (:obj:`str`):
            Sticker set title; 1-64 characters

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSuggestedStickerSetName"

    def __init__(self, title, extra=None, **kwargs):
        self.extra = extra
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "GetSuggestedStickerSetName":
        title = q.get('title')
        return GetSuggestedStickerSetName(title)
