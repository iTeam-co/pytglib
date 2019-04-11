

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
    def read(q: dict, *args) -> "ChatActionStartPlayingGame or ChatActionCancel or ChatActionUploadingVideo or ChatActionRecordingVideoNote or ChatActionUploadingPhoto or ChatActionTyping or ChatActionUploadingVideoNote or ChatActionRecordingVoiceNote or ChatActionUploadingVoiceNote or ChatActionChoosingLocation or ChatActionUploadingDocument or ChatActionChoosingContact or ChatActionRecordingVideo":
        if q.get("@type"):
            return Object.read(q)
        return ChatAction()
