

from ..utils import Object


class UploadFile(Object):
    """
    Asynchronously uploads a file to the cloud without sending it in a message. updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message 

    Attributes:
        ID (:obj:`str`): ``UploadFile``

    Args:
        file (:class:`telegram.api.types.InputFile`):
            File to upload 
        file_type (:class:`telegram.api.types.FileType`):
            File type
        priority (:obj:`int`):
            Priority of the upload (1-32)The higher the priority, the earlier the file will be uploadedIf the priorities of two files are equal, then the first one for which uploadFile was called will be uploaded first

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "uploadFile"

    def __init__(self, file, file_type, priority, extra=None, **kwargs):
        self.extra = extra
        self.file = file  # InputFile
        self.file_type = file_type  # FileType
        self.priority = priority  # int

    @staticmethod
    def read(q: dict, *args) -> "UploadFile":
        file = Object.read(q.get('file'))
        file_type = Object.read(q.get('file_type'))
        priority = q.get('priority')
        return UploadFile(file, file_type, priority)
