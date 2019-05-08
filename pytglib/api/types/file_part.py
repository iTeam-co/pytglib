

from ..utils import Object


class FilePart(Object):
    """
    Contains a part of a file 

    Attributes:
        ID (:obj:`str`): ``FilePart``

    Args:
        data (:obj:`bytes`):
            File bytes

    Returns:
        FilePart

    Raises:
        :class:`telegram.Error`
    """
    ID = "filePart"

    def __init__(self, data, **kwargs):
        
        self.data = data  # bytes

    @staticmethod
    def read(q: dict, *args) -> "FilePart":
        data = q.get('data')
        return FilePart(data)
