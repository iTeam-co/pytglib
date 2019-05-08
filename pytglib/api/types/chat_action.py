

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
    def read(q: dict, *args) -> "ChatActionUploadingVideo or ChatActionRecordingVideoNote or ChatActionTyping or ChatActionRecordingVideo or ChatActionUploadingVideoNote or ChatActionUploadingDocument or ChatActionCancel or ChatActionUploadingPhoto or ChatActionRecordingVoiceNote or ChatActionStartPlayingGame or ChatActionUploadingVoiceNote or ChatActionChoosingContact or ChatActionChoosingLocation":
        if q.get("@type"):
            return Object.read(q)
        return ChatAction()
