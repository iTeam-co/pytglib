

from ..utils import Object


class SetStickerSetThumbnail(Object):
    """
    Sets a sticker set thumbnail; for bots only. Returns the sticker set

    Attributes:
        ID (:obj:`str`): ``SetStickerSetThumbnail``

    Args:
        user_id (:obj:`int`):
            Sticker set owner 
        name (:obj:`str`):
            Sticker set name
        thumbnail (:class:`telegram.api.types.InputFile`):
            Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnailThumbnail format must match the format of stickers in the set

    Returns:
        StickerSet

    Raises:
        :class:`telegram.Error`
    """
    ID = "setStickerSetThumbnail"

    def __init__(self, user_id, name, thumbnail, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.name = name  # str
        self.thumbnail = thumbnail  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "SetStickerSetThumbnail":
        user_id = q.get('user_id')
        name = q.get('name')
        thumbnail = Object.read(q.get('thumbnail'))
        return SetStickerSetThumbnail(user_id, name, thumbnail)
