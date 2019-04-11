

from ..utils import Object


class ChatActionUploadingVideo(Object):
    """
    The user is uploading a video 

    Attributes:
        ID (:obj:`str`): ``ChatActionUploadingVideo``

    Args:
        progress (:obj:`int`):
            Upload progress, as a percentage

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionUploadingVideo"

    def __init__(self, progress, **kwargs):
        
        self.progress = progress  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionUploadingVideo":
        progress = q.get('progress')
        return ChatActionUploadingVideo(progress)
