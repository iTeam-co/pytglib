

from ..utils import Object


class UpdateChatVideoChat(Object):
    """
    A chat video chat state has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatVideoChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        video_chat (:class:`telegram.api.types.videoChat`):
            New value of video_chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatVideoChat"

    def __init__(self, chat_id, video_chat, **kwargs):
        
        self.chat_id = chat_id  # int
        self.video_chat = video_chat  # VideoChat

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatVideoChat":
        chat_id = q.get('chat_id')
        video_chat = Object.read(q.get('video_chat'))
        return UpdateChatVideoChat(chat_id, video_chat)
