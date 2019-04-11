

from ..utils import Object


class SavedCredentials(Object):
    """
    Contains information about saved card credentials 

    Attributes:
        ID (:obj:`str`): ``SavedCredentials``

    Args:
        id (:obj:`str`):
            Unique identifier of the saved credentials 
        title (:obj:`str`):
            Title of the saved credentials

    Returns:
        SavedCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "savedCredentials"

    def __init__(self, id, title, **kwargs):
        
        self.id = id  # str
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "SavedCredentials":
        id = q.get('id')
        title = q.get('title')
        return SavedCredentials(id, title)
