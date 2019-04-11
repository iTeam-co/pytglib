

from ..utils import Object


class ChatActionUploadingDocument(Object):
    """
    The user is uploading a document 

    Attributes:
        ID (:obj:`str`): ``ChatActionUploadingDocument``

    Args:
        progress (:obj:`int`):
            Upload progress, as a percentage

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionUploadingDocument"

    def __init__(self, progress, **kwargs):
        
        self.progress = progress  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionUploadingDocument":
        progress = q.get('progress')
        return ChatActionUploadingDocument(progress)
