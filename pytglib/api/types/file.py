

from ..utils import Object


class File(Object):
    """
    Represents a file

    Attributes:
        ID (:obj:`str`): ``File``

    Args:
        id (:obj:`int`):
            Unique file identifier
        size (:obj:`int`):
            File size; 0 if unknown
        expected_size (:obj:`int`):
            Expected file size in case the exact file size is unknown, but an approximate size is knownCan be used to show download/upload progress
        local (:class:`telegram.api.types.localFile`):
            Information about the local copy of the file
        remote (:class:`telegram.api.types.remoteFile`):
            Information about the remote copy of the file

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "file"

    def __init__(self, id, size, expected_size, local, remote, **kwargs):
        
        self.id = id  # int
        self.size = size  # int
        self.expected_size = expected_size  # int
        self.local = local  # LocalFile
        self.remote = remote  # RemoteFile

    @staticmethod
    def read(q: dict, *args) -> "File":
        id = q.get('id')
        size = q.get('size')
        expected_size = q.get('expected_size')
        local = Object.read(q.get('local'))
        remote = Object.read(q.get('remote'))
        return File(id, size, expected_size, local, remote)
