

from ..utils import Object


class PassportElementErrorSourceTranslationFiles(Object):
    """
    The translation of the document contains an error. The error will be considered resolved when the list of translation files changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceTranslationFiles``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceTranslationFiles"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceTranslationFiles":
        
        return PassportElementErrorSourceTranslationFiles()
