

from ..utils import Object


class PassportElementErrorSourceTranslationFile(Object):
    """
    One of files with the translation of the document contains an error. The error will be considered resolved when the file changes 

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceTranslationFile``

    Args:
        file_index (:obj:`int`):
            Index of a file with the error

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceTranslationFile"

    def __init__(self, file_index, **kwargs):
        
        self.file_index = file_index  # int

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceTranslationFile":
        file_index = q.get('file_index')
        return PassportElementErrorSourceTranslationFile(file_index)
