

from ..utils import Object


class FileTypeSticker(Object):
    """
    The file is a sticker

    Attributes:
        ID (:obj:`str`): ``FileTypeSticker``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeSticker"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeSticker":
        
        return FileTypeSticker()
