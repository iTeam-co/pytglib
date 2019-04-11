

from ..utils import Object


class UpdateUserChatAction(Object):
    """
    User activity in the chat has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateUserChatAction``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            Identifier of a user performing an action 
        action (:class:`telegram.api.types.ChatAction`):
            The action description

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUserChatAction"

    def __init__(self, chat_id, user_id, action, **kwargs):
        
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.action = action  # ChatAction

    @staticmethod
    def read(q: dict, *args) -> "UpdateUserChatAction":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        action = Object.read(q.get('action'))
        return UpdateUserChatAction(chat_id, user_id, action)
