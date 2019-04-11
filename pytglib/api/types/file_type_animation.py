

from ..utils import Object


class FileTypeAnimation(Object):
    """
    The file is an animation

    Attributes:
        ID (:obj:`str`): ``FileTypeAnimation``

    No parameters required.

    Returns:
        FileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileTypeAnimation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "FileTypeAnimation":
        
        return FileTypeAnimation()
