

from ..utils import Object


class GetAttachedStickerSets(Object):
    """
    Returns a list of sticker sets attached to a file. Currently only photos and videos can have attached sticker sets 

    Attributes:
        ID (:obj:`str`): ``GetAttachedStickerSets``

    Args:
        file_id (:obj:`int`):
            File identifier

    Returns:
        StickerSets

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAttachedStickerSets"

    def __init__(self, file_id, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetAttachedStickerSets":
        file_id = q.get('file_id')
        return GetAttachedStickerSets(file_id)
