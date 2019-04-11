

from ..utils import Object


class FileTypeVideo(Object):
    """
    The file is a video

    Attributes:
        ID (:obj:`str`): ``FileTypeVideo``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeVideo":
        
        return FileTypeVideo()
