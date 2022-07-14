

from ..utils import Object


class FileDownload(Object):
    """
    Describes a file added to file download list

    Attributes:
        ID (:obj:`str`): ``FileDownload``

    Args:
        file_id (:obj:`int`):
            File identifier
        message (:class:`telegram.api.types.message`):
            The message with the file
        add_date (:obj:`int`):
            Point in time (Unix timestamp) when the file was added to the download list
        complete_date (:obj:`int`):
            Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
        is_paused (:obj:`bool`):
            True, if downloading of the file is paused

    Returns:
        FileDownload

    Raises:
        :class:`telegram.Error`
    """
    ID = "fileDownload"

    def __init__(self, file_id, message, add_date, complete_date, is_paused, **kwargs):
        
        self.file_id = file_id  # int
        self.message = message  # Message
        self.add_date = add_date  # int
        self.complete_date = complete_date  # int
        self.is_paused = is_paused  # bool

    @staticmethod
    def read(q: dict, *args) -> "FileDownload":
        file_id = q.get('file_id')
        message = Object.read(q.get('message'))
        add_date = q.get('add_date')
        complete_date = q.get('complete_date')
        is_paused = q.get('is_paused')
        return FileDownload(file_id, message, add_date, complete_date, is_paused)
