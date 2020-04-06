

from ..utils import Object


class InputFileRemote(Object):
    """
    A file defined by its remote ID. The remote ID is guaranteed to be usable only if the corresponding file is still accessible to the user and known to TDLib.For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the client

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
