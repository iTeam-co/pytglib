

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
    def read(q: dict, *args) -> "ChatActionStartPlayingGame or ChatActionChoosingLocation or ChatActionUploadingVideoNote or ChatActionUploadingVideo or ChatActionRecordingVideoNote or ChatActionRecordingVoiceNote or ChatActionUploadingVoiceNote or ChatActionTyping or ChatActionUploadingDocument or ChatActionChoosingContact or ChatActionRecordingVideo or ChatActionUploadingPhoto or ChatActionCancel":
        if q.get("@type"):
            return Object.read(q)
        return ChatAction()
