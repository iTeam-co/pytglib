

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
    def read(q: dict, *args) -> "FileTypeNone or FileTypeVideoNote or FileTypeSecret or FileTypeVoiceNote or FileTypeThumbnail or FileTypeAnimation or FileTypeSticker or FileTypeUnknown or FileTypeVideo or FileTypeAudio or FileTypeSecretThumbnail or FileTypeSecure or FileTypeDocument or FileTypeWallpaper or FileTypeProfilePhoto or FileTypePhoto":
        if q.get("@type"):
            return Object.read(q)
        return FileType()
