

from ..utils import Object


class UpdateNewChat(Object):
    """
    A new chat has been loaded/created. This update is guaranteed to come before the chat identifier is returned to the client. The chat field changes will be reported through separate updates 

    Attributes:
        ID (:obj:`str`): ``UpdateNewChat``

    Args:
        chat (:class:`telegram.api.types.chat`):
            The chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewChat"

    def __init__(self, chat, **kwargs):
        
        self.chat = chat  # Chat

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewChat":
        chat = Object.read(q.get('chat'))
        return UpdateNewChat(chat)
