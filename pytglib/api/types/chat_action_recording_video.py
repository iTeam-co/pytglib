

from ..utils import Object


class ChatActionRecordingVideo(Object):
    """
    The user is recording a video

    Attributes:
        ID (:obj:`str`): ``ChatActionRecordingVideo``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionRecordingVideo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionRecordingVideo":
        
        return ChatActionRecordingVideo()
