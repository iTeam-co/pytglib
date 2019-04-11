

from ..utils import Object


class InputPersonalDocument(Object):
    """
    A personal document to be saved to Telegram Passport 

    Attributes:
        ID (:obj:`str`): ``InputPersonalDocument``

    Args:
        files (List of :class:`telegram.api.types.InputFile`):
            List of files containing the pages of the document 
        translation (List of :class:`telegram.api.types.InputFile`):
            List of files containing a certified English translation of the document

    Returns:
        InputPersonalDocument

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPersonalDocument"

    def __init__(self, files, translation, **kwargs):
        
        self.files = files  # list of InputFile
        self.translation = translation  # list of InputFile

    @staticmethod
    def read(q: dict, *args) -> "InputPersonalDocument":
        files = [Object.read(i) for i in q.get('files', [])]
        translation = [Object.read(i) for i in q.get('translation', [])]
        return InputPersonalDocument(files, translation)
