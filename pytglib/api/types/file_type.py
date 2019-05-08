

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
    def read(q: dict, *args) -> "FileTypeNone or FileTypeUnknown or FileTypeVideo or FileTypeSticker or FileTypeVoiceNote or FileTypeDocument or FileTypeSecret or FileTypeSecure or FileTypeAudio or FileTypeWallpaper or FileTypeAnimation or FileTypeThumbnail or FileTypeProfilePhoto or FileTypeVideoNote or FileTypePhoto or FileTypeSecretThumbnail":
        if q.get("@type"):
            return Object.read(q)
        return FileType()
