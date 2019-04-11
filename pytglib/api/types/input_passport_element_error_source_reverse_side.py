

from ..utils import Object


class InputPassportElementErrorSourceReverseSide(Object):
    """
    The reverse side of the document contains an error. The error is considered resolved when the file with the reverse side of the document changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceReverseSide``

    Args:
        file_hash (:obj:`bytes`):
            Current hash of the file containing the reverse side

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceReverseSide"

    def __init__(self, file_hash, **kwargs):
        
        self.file_hash = file_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceReverseSide":
        file_hash = q.get('file_hash')
        return InputPassportElementErrorSourceReverseSide(file_hash)
