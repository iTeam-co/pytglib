

from ..utils import Object


class GetMessageFileType(Object):
    """
    Returns information about a file with messages exported from another application 

    Attributes:
        ID (:obj:`str`): ``GetMessageFileType``

    Args:
        message_file_head (:obj:`str`):
            Beginning of the message file; up to 100 first lines

    Returns:
        MessageFileType

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageFileType"

    def __init__(self, message_file_head, extra=None, **kwargs):
        self.extra = extra
        self.message_file_head = message_file_head  # str

    @staticmethod
    def read(q: dict, *args) -> "GetMessageFileType":
        message_file_head = q.get('message_file_head')
        return GetMessageFileType(message_file_head)
