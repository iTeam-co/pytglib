

from ..utils import Object


class GetSuggestedFileName(Object):
    """
    Returns suggested name for saving a file in a given directory 

    Attributes:
        ID (:obj:`str`): ``GetSuggestedFileName``

    Args:
        file_id (:obj:`int`):
            Identifier of the file 
        directory (:obj:`str`):
            Directory in which the file is supposed to be saved

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSuggestedFileName"

    def __init__(self, file_id, directory, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.directory = directory  # str

    @staticmethod
    def read(q: dict, *args) -> "GetSuggestedFileName":
        file_id = q.get('file_id')
        directory = q.get('directory')
        return GetSuggestedFileName(file_id, directory)
