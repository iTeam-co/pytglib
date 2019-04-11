

from ..utils import Object


class GetFile(Object):
    """
    Returns information about a file; this is an offline request 

    Attributes:
        ID (:obj:`str`): ``GetFile``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to get

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "getFile"

    def __init__(self, file_id, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetFile":
        file_id = q.get('file_id')
        return GetFile(file_id)
