

from ..utils import Object


class PersonalDocument(Object):
    """
    A personal document, containing some information about a user 

    Attributes:
        ID (:obj:`str`): ``PersonalDocument``

    Args:
        files (List of :class:`telegram.api.types.datedFile`):
            List of files containing the pages of the document 
        translation (List of :class:`telegram.api.types.datedFile`):
            List of files containing a certified English translation of the document

    Returns:
        PersonalDocument

    Raises:
        :class:`telegram.Error`
    """
    ID = "personalDocument"

    def __init__(self, files, translation, **kwargs):
        
        self.files = files  # list of datedFile
        self.translation = translation  # list of datedFile

    @staticmethod
    def read(q: dict, *args) -> "PersonalDocument":
        files = [Object.read(i) for i in q.get('files', [])]
        translation = [Object.read(i) for i in q.get('translation', [])]
        return PersonalDocument(files, translation)
