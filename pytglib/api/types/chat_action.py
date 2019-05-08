

from ..utils import Object


class ChatAction(Object):
    """
    Describes the different types of activity in a chat

    No parameters required.
    """
    ID = "chatAction"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionCancel or ChatActionRecordingVideoNote or ChatActionUploadingVideoNote or ChatActionRecordingVoiceNote or ChatActionChoosingContact or ChatActionTyping or ChatActionChoosingLocation or ChatActionRecordingVideo or ChatActionUploadingPhoto or ChatActionUploadingVideo or ChatActionStartPlayingGame or ChatActionUploadingVoiceNote or ChatActionUploadingDocument":
        if q.get("@type"):
            return Object.read(q)
        return ChatAction()
