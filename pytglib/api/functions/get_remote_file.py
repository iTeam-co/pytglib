

from ..utils import Object


class GetRemoteFile(Object):
    """
    Returns information about a file by its remote ID; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message 

    Attributes:
        ID (:obj:`str`): ``GetRemoteFile``

    Args:
        remote_file_id (:obj:`str`):
            Remote identifier of the file to get 
        file_type (:class:`telegram.api.types.FileType`):
            File type, if known

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRemoteFile"

    def __init__(self, remote_file_id, file_type, extra=None, **kwargs):
        self.extra = extra
        self.remote_file_id = remote_file_id  # str
        self.file_type = file_type  # FileType

    @staticmethod
    def read(q: dict, *args) -> "GetRemoteFile":
        remote_file_id = q.get('remote_file_id')
        file_type = Object.read(q.get('file_type'))
        return GetRemoteFile(remote_file_id, file_type)
