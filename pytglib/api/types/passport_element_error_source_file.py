

from ..utils import Object


class PassportElementErrorSourceFile(Object):
    """
    The file contains an error. The error will be considered resolved when the file changes 

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceFile``

    Args:
        file_index (:obj:`int`):
            Index of a file with the error

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceFile"

    def __init__(self, file_index, **kwargs):
        
        self.file_index = file_index  # int

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceFile":
        file_index = q.get('file_index')
        return PassportElementErrorSourceFile(file_index)
