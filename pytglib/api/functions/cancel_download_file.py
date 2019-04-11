

from ..utils import Object


class CancelDownloadFile(Object):
    """
    Stops the downloading of a file. If a file has already been downloaded, does nothing 

    Attributes:
        ID (:obj:`str`): ``CancelDownloadFile``

    Args:
        file_id (:obj:`int`):
            Identifier of a file to stop downloading 
        only_if_pending (:obj:`bool`):
            Pass true to stop downloading only if it hasn't been started, ierequest hasn't been sent to server

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "cancelDownloadFile"

    def __init__(self, file_id, only_if_pending, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.only_if_pending = only_if_pending  # bool

    @staticmethod
    def read(q: dict, *args) -> "CancelDownloadFile":
        file_id = q.get('file_id')
        only_if_pending = q.get('only_if_pending')
        return CancelDownloadFile(file_id, only_if_pending)
