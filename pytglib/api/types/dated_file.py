

from ..utils import Object


class DatedFile(Object):
    """
    File with the date it was uploaded 

    Attributes:
        ID (:obj:`str`): ``DatedFile``

    Args:
        file (:class:`telegram.api.types.file`):
            The file 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the file was uploaded

    Returns:
        DatedFile

    Raises:
        :class:`telegram.Error`
    """
    ID = "datedFile"

    def __init__(self, file, date, **kwargs):
        
        self.file = file  # File
        self.date = date  # int

    @staticmethod
    def read(q: dict, *args) -> "DatedFile":
        file = Object.read(q.get('file'))
        date = q.get('date')
        return DatedFile(file, date)
