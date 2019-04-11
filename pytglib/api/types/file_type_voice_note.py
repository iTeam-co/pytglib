

from ..utils import Object


class FileTypeVoiceNote(Object):
    """
    The file is a voice note

    Attributes:
        ID (:obj:`str`): ``FileTypeVoiceNote``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeVoiceNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeVoiceNote":
        
        return FileTypeVoiceNote()
