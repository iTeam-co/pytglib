

from ..utils import Object


class InputPassportElementErrorSourceSelfie(Object):
    """
    The selfie contains an error. The error is considered resolved when the file with the selfie changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceSelfie``

    Args:
        file_hash (:obj:`bytes`):
            Current hash of the file containing the selfie

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceSelfie"

    def __init__(self, file_hash, **kwargs):
        
        self.file_hash = file_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceSelfie":
        file_hash = q.get('file_hash')
        return InputPassportElementErrorSourceSelfie(file_hash)
