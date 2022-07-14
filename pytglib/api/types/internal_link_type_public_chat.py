

from ..utils import Object


class InternalLinkTypePublicChat(Object):
    """
    The link is a link to a chat by its username. Call searchPublicChat with the given chat username to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypePublicChat``

    Args:
        chat_username (:obj:`str`):
            Username of the chat

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypePublicChat"

    def __init__(self, chat_username, **kwargs):
        
        self.chat_username = chat_username  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypePublicChat":
        chat_username = q.get('chat_username')
        return InternalLinkTypePublicChat(chat_username)
