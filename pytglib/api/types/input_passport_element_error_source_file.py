

from ..utils import Object


class InputPassportElementErrorSourceFile(Object):
    """
    The file contains an error. The error is considered resolved when the file changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceFile``

    Args:
        file_hash (:obj:`bytes`):
            Current hash of the file which has the error

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceFile"

    def __init__(self, file_hash, **kwargs):
        
        self.file_hash = file_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceFile":
        file_hash = q.get('file_hash')
        return InputPassportElementErrorSourceFile(file_hash)
