

from ..utils import Object


class ChatActionUploadingVideoNote(Object):
    """
    The user is uploading a video note 

    Attributes:
        ID (:obj:`str`): ``ChatActionUploadingVideoNote``

    Args:
        progress (:obj:`int`):
            Upload progress, as a percentage

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionUploadingVideoNote"

    def __init__(self, progress, **kwargs):
        
        self.progress = progress  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionUploadingVideoNote":
        progress = q.get('progress')
        return ChatActionUploadingVideoNote(progress)
