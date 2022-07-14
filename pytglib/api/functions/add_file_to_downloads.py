

from ..utils import Object


class AddFileToDownloads(Object):
    """
    Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates.If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file

    Attributes:
        ID (:obj:`str`): ``AddFileToDownloads``

    Args:
        file_id (:obj:`int`):
            Identifier of the file to download
        chat_id (:obj:`int`):
            Chat identifier of the message with the file
        message_id (:obj:`int`):
            Message identifier
        priority (:obj:`int`):
            Priority of the download (1-32)The higher the priority, the earlier the file will be downloadedIf the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "addFileToDownloads"

    def __init__(self, file_id, chat_id, message_id, priority, extra=None, **kwargs):
        self.extra = extra
        self.file_id = file_id  # int
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.priority = priority  # int

    @staticmethod
    def read(q: dict, *args) -> "AddFileToDownloads":
        file_id = q.get('file_id')
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        priority = q.get('priority')
        return AddFileToDownloads(file_id, chat_id, message_id, priority)
