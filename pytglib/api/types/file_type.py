

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
    def read(q: dict, *args) -> "FileTypeProfilePhoto or FileTypeSecretThumbnail or FileTypeVoiceNote or FileTypeSecret or FileTypeVideoNote or FileTypeSticker or FileTypeThumbnail or FileTypeSecure or FileTypeVideo or FileTypeNone or FileTypeAnimation or FileTypeWallpaper or FileTypeDocument or FileTypeAudio or FileTypeUnknown or FileTypePhoto":
        if q.get("@type"):
            return Object.read(q)
        return FileType()
