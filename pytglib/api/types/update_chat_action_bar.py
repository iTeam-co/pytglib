

from ..utils import Object


class UpdateChatActionBar(Object):
    """
    The chat action bar was changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatActionBar``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        action_bar (:class:`telegram.api.types.ChatActionBar`):
            The new value of the action bar; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatActionBar"

    def __init__(self, chat_id, action_bar, **kwargs):
        
        self.chat_id = chat_id  # int
        self.action_bar = action_bar  # ChatActionBar

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatActionBar":
        chat_id = q.get('chat_id')
        action_bar = Object.read(q.get('action_bar'))
        return UpdateChatActionBar(chat_id, action_bar)
