

from ..utils import Object


class ChatActionUploadingPhoto(Object):
    """
    The user is uploading a photo 

    Attributes:
        ID (:obj:`str`): ``ChatActionUploadingPhoto``

    Args:
        progress (:obj:`int`):
            Upload progress, as a percentage

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionUploadingPhoto"

    def __init__(self, progress, **kwargs):
        
        self.progress = progress  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionUploadingPhoto":
        progress = q.get('progress')
        return ChatActionUploadingPhoto(progress)
