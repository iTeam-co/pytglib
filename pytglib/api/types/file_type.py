

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
    def read(q: dict, *args) -> "FileTypeNone or FileTypeDocument or FileTypeVideo or FileTypeVideoNote or FileTypeSecret or FileTypeAudio or FileTypeVoiceNote or FileTypeAnimation or FileTypeWallpaper or FileTypeUnknown or FileTypeSecure or FileTypeProfilePhoto or FileTypeSticker or FileTypePhoto or FileTypeThumbnail or FileTypeSecretThumbnail":
        if q.get("@type"):
            return Object.read(q)
        return FileType()
