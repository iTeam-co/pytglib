

from ..utils import Object


class DeleteFile(Object):
    """
    Deletes a file from the TDLib file cache 

    Attributes:
        ID (:obj:`str`): ``DeleteFile``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteFile"

    def __init__(self, file_id, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteFile":
        file_id = q.get('file_id')
        return DeleteFile(file_id)
