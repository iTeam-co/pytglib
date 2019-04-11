

from ..utils import Object


class InputFileRemote(Object):
    """
    A file defined by its remote ID 

    Attributes:
        ID (:obj:`str`): ``InputFileRemote``

    Args:
        id (:obj:`str`):
            Remote file identifier

    Returns:
        InputFile

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputFileRemote"

    def __init__(self, id, **kwargs):
        
        self.id = id  # str

    @staticmethod
    def read(q: dict, *args) -> "InputFileRemote":
        id = q.get('id')
        return InputFileRemote(id)
