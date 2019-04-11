

from ..utils import Object


class InputPassportElementErrorSourceTranslationFiles(Object):
    """
    The translation of the document contains an error. The error is considered resolved when the list of files changes 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementErrorSourceTranslationFiles``

    Args:
        file_hashes (List of :obj:`bytes`):
            Current hashes of all files with the translation

    Returns:
        InputPassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementErrorSourceTranslationFiles"

    def __init__(self, file_hashes, **kwargs):
        
        self.file_hashes = file_hashes  # list of bytes

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementErrorSourceTranslationFiles":
        file_hashes = q.get('file_hashes')
        return InputPassportElementErrorSourceTranslationFiles(file_hashes)
