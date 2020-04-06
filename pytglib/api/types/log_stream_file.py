

from ..utils import Object


class LogStreamFile(Object):
    """
    The log is written to a file 

    Attributes:
        ID (:obj:`str`): ``LogStreamFile``

    Args:
        path (:obj:`str`):
            Path to the file to where the internal TDLib log will be written 
        max_file_size (:obj:`int`):
            The maximum size of the file to where the internal TDLib log is written before the file will be auto-rotated

    Returns:
        LogStream

    Raises:
        :class:`telegram.Error`
    """
    ID = "logStreamFile"

    def __init__(self, path, max_file_size, **kwargs):
        
        self.path = path  # str
        self.max_file_size = max_file_size  # int

    @staticmethod
    def read(q: dict, *args) -> "LogStreamFile":
        path = q.get('path')
        max_file_size = q.get('max_file_size')
        return LogStreamFile(path, max_file_size)
