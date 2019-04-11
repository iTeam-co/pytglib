

from ..utils import Object


class InputFileLocal(Object):
    """
    A file defined by a local path 

    Attributes:
        ID (:obj:`str`): ``InputFileLocal``

    Args:
        path (:obj:`str`):
            Local path to the file

    Returns:
        InputFile

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputFileLocal"

    def __init__(self, path, **kwargs):
        
        self.path = path  # str

    @staticmethod
    def read(q: dict, *args) -> "InputFileLocal":
        path = q.get('path')
        return InputFileLocal(path)
