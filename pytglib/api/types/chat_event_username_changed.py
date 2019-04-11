

from ..utils import Object


class ChatEventUsernameChanged(Object):
    """
    The chat username was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventUsernameChanged``

    Args:
        old_username (:obj:`str`):
            Previous chat username 
        new_username (:obj:`str`):
            New chat username

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventUsernameChanged"

    def __init__(self, old_username, new_username, **kwargs):
        
        self.old_username = old_username  # str
        self.new_username = new_username  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatEventUsernameChanged":
        old_username = q.get('old_username')
        new_username = q.get('new_username')
        return ChatEventUsernameChanged(old_username, new_username)
