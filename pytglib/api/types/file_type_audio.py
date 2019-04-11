

from ..utils import Object


class FileTypeAudio(Object):
    """
    The file is an audio file

    Attributes:
        ID (:obj:`str`): ``FileTypeAudio``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeAudio"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeAudio":
        
        return FileTypeAudio()
