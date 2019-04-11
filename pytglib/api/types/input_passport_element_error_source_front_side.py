

from ..utils import Object


class InputPassportElementErrorSourceFrontSide(Object):
    """
    The front side of the document contains an error. The error is considered resolved when the file with the front side of the document changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceFrontSide``

    Args:
        file_hash (:obj:`bytes`):
            Current hash of the file containing the front side

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceFrontSide"

    def __init__(self, file_hash, **kwargs):
        
        self.file_hash = file_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceFrontSide":
        file_hash = q.get('file_hash')
        return InputPassportElementErrorSourceFrontSide(file_hash)
