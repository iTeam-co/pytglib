

from ..utils import Object


class ChatActionRecordingVideoNote(Object):
    """
    The user is recording a video note

    Attributes:
        ID (:obj:`str`): ``ChatActionRecordingVideoNote``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionRecordingVideoNote"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionRecordingVideoNote":
        
        return ChatActionRecordingVideoNote()
