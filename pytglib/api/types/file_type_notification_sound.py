

from ..utils import Object


class FileTypeNotificationSound(Object):
    """
    The file is a notification sound

    Attributes:
        ID (:obj:`str`): ``FileTypeNotificationSound``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeNotificationSound"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeNotificationSound":
        
        return FileTypeNotificationSound()
