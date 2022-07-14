

from ..utils import Object


class UploadStickerFile(Object):
    """
    Uploads a file with a sticker; returns the uploaded file 

    Attributes:
        ID (:obj:`str`): ``UploadStickerFile``

    Args:
        user_id (:obj:`int`):
            Sticker file owner; ignored for regular users 
        sticker (:class:`telegram.api.types.inputSticker`):
            Sticker file to upload

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "uploadStickerFile"

    def __init__(self, user_id, sticker, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.sticker = sticker  # InputSticker

    @staticmethod
    def read(q: dict, *args) -> "UploadStickerFile":
        user_id = q.get('user_id')
        sticker = Object.read(q.get('sticker'))
        return UploadStickerFile(user_id, sticker)
