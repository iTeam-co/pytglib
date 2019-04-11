

from ..utils import Object


class InputPassportElementErrorSourceTranslationFile(Object):
    """
    One of the files containing the translation of the document contains an error. The error is considered resolved when the file with the translation changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceTranslationFile``

    Args:
        file_hash (:obj:`bytes`):
            Current hash of the file containing the translation

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceTranslationFile"

    def __init__(self, file_hash, **kwargs):
        
        self.file_hash = file_hash  # bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceTranslationFile":
        file_hash = q.get('file_hash')
        return InputPassportElementErrorSourceTranslationFile(file_hash)
