

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
            Pass true to create a channel chat
        description (:obj:`str`):
            Chat description; 0-255 characters
        location (:class:`telegram.api.types.chatLocation`):
            Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat
        for_import (:obj:`bool`):
            Pass true to create a supergroup for importing messages using importMessage

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewSupergroupChat"

    def __init__(self, title, is_channel, description, location, for_import, extra=None, **kwargs):
        self.extra = extra
        self.title = title  # str
        self.is_channel = is_channel  # bool
        self.description = description  # str
        self.location = location  # ChatLocation
        self.for_import = for_import  # bool

    @staticmethod
    def read(q: dict, *args) -> "CreateNewSupergroupChat":
        title = q.get('title')
        is_channel = q.get('is_channel')
        description = q.get('description')
        location = Object.read(q.get('location'))
        for_import = q.get('for_import')
        return CreateNewSupergroupChat(title, is_channel, description, location, for_import)
