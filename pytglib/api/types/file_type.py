

from ..utils import Object


class FileType(Object):
    """
    Represents the type of a file

    No parameters required.
    """
    ID = "fileType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeVideo or FileTypeUnknown or FileTypeVideoNote or FileTypeSticker or FileTypeAudio or FileTypeNone or FileTypeSecret or FileTypeThumbnail or FileTypeDocument or FileTypeProfilePhoto or FileTypeNotificationSound or FileTypeSecretThumbnail or FileTypeVoiceNote or FileTypeWallpaper or FileTypePhoto or FileTypeAnimation or FileTypeSecure":
        if q.get("@type"):
            return Object.read(q)
        return FileType()
