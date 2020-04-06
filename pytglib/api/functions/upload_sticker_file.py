

from ..utils import Object


class UploadStickerFile(Object):
    """
    Uploads a PNG image with a sticker; for bots only; returns the uploaded file

    Attributes:
        ID (:obj:`str`): ``UploadStickerFile``

    Args:
        user_id (:obj:`int`):
            Sticker file owner 
        png_sticker (:class:`telegram.api.types.InputFile`):
            PNG image with the sticker; must be up to 512 KB in size and fit in 512x512 square

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "uploadStickerFile"

    def __init__(self, user_id, png_sticker, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.png_sticker = png_sticker  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "UploadStickerFile":
        user_id = q.get('user_id')
        png_sticker = Object.read(q.get('png_sticker'))
        return UploadStickerFile(user_id, png_sticker)
