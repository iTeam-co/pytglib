

from ..utils import Object


class CancelUploadFile(Object):
    """
    Stops the uploading of a file. Supported only for files uploaded by using uploadFile. For other files the behavior is undefined 

    Attributes:
        ID (:obj:`str`): ``CancelUploadFile``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to stop uploading

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "cancelUploadFile"

    def __init__(self, file_id, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CancelUploadFile":
        file_id = q.get('file_id')
        return CancelUploadFile(file_id)
