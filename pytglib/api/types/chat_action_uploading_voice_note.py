

from ..utils import Object


class ChatActionUploadingVoiceNote(Object):
    """
    The user is uploading a voice note 

    Attributes:
        ID (:obj:`str`): ``ChatActionUploadingVoiceNote``

    Args:
        progress (:obj:`int`):
            Upload progress, as a percentage

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionUploadingVoiceNote"

    def __init__(self, progress, **kwargs):
        
        self.progress = progress  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatActionUploadingVoiceNote":
        progress = q.get('progress')
        return ChatActionUploadingVoiceNote(progress)
