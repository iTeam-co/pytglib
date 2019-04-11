

from ..utils import Object


class UpdateFile(Object):
    """
    Information about a file was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateFile``

    Args:
        file (:class:`telegram.api.types.file`):
            New data about the file

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateFile"

    def __init__(self, file, **kwargs):
        
        self.file = file  # File

    @staticmethod
    def read(q: dict, *args) -> "UpdateFile":
        file = Object.read(q.get('file'))
        return UpdateFile(file)
