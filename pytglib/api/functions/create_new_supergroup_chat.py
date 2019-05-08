

from ..utils import Object


class CreateNewSupergroupChat(Object):
    """
    Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat 

    Attributes:
        ID (:obj:`str`): ``CreateNewSupergroupChat``

    Args:
        title (:obj:`str`):
            Title of the new chat; 1-128 characters 
        is_channel (:obj:`bool`):
            True, if a channel chat should be created 
        description (:obj:`str`):
            Chat description; 0-255 characters

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewSupergroupChat"

    def __init__(self, title, is_channel, description, extra=None, **kwargs):
        self.extra = extra
        self.title = title  # str
        self.is_channel = is_channel  # bool
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "CreateNewSupergroupChat":
        title = q.get('title')
        is_channel = q.get('is_channel')
        description = q.get('description')
        return CreateNewSupergroupChat(title, is_channel, description)
