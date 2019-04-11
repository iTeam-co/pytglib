

from ..utils import Object


class ChatActionRecordingVoiceNote(Object):
    """
    The user is recording a voice note

    Attributes:
        ID (:obj:`str`): ``ChatActionRecordingVoiceNote``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionRecordingVoiceNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionRecordingVoiceNote":
        
        return ChatActionRecordingVoiceNote()
