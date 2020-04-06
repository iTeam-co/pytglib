

from ..utils import Object


class ChatAdministrator(Object):
    """
    Contains information about a chat administrator 

    Attributes:
        ID (:obj:`str`): ``ChatAdministrator``

    Args:
        user_id (:obj:`int`):
            User identifier of the administrator 
        custom_title (:obj:`str`):
            Custom title of the administrator 
        is_owner (:obj:`bool`):
            True, if the user is the owner of the chat

    Returns:
        ChatAdministrator

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatAdministrator"

    def __init__(self, user_id, custom_title, is_owner, **kwargs):
        
        self.user_id = user_id  # int
        self.custom_title = custom_title  # str
        self.is_owner = is_owner  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatAdministrator":
        user_id = q.get('user_id')
        custom_title = q.get('custom_title')
        is_owner = q.get('is_owner')
        return ChatAdministrator(user_id, custom_title, is_owner)
