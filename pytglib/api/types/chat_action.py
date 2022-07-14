

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
    def read(q: dict, *args) -> "ChatActionRecordingVoiceNote or ChatActionRecordingVideoNote or ChatActionChoosingContact or ChatActionUploadingVoiceNote or ChatActionTyping or ChatActionChoosingSticker or ChatActionUploadingDocument or ChatActionRecordingVideo or ChatActionChoosingLocation or ChatActionStartPlayingGame or ChatActionUploadingVideoNote or ChatActionWatchingAnimations or ChatActionCancel or ChatActionUploadingPhoto or ChatActionUploadingVideo":
        if q.get("@type"):
            return Object.read(q)
        return ChatAction()
