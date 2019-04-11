

from ..utils import Object


class PassportElementErrorSourceTranslationFile(Object):
    """
    One of files with the translation of the document contains an error. The error will be considered resolved when the file changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceTranslationFile``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceTranslationFile"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceTranslationFile":
        
        return PassportElementErrorSourceTranslationFile()
