

from ..utils import Object


class MessageLinkInfo(Object):
    """
    Contains information about a link to a message in a chat

    Attributes:
        ID (:obj:`str`): ``MessageLinkInfo``

    Args:
        is_public (:obj:`bool`):
            True, if the link is a public link for a message in a chat
        chat_id (:obj:`int`):
            If found, identifier of the chat to which the message belongs, 0 otherwise
        message (:class:`telegram.api.types.message`):
            If found, the linked message; may be null
        for_album (:obj:`bool`):
            True, if the whole media album to which the message belongs is linked

    Returns:
        MessageLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageLinkInfo"

    def __init__(self, is_public, chat_id, message, for_album, **kwargs):
        
        self.is_public = is_public  # bool
        self.chat_id = chat_id  # int
        self.message = message  # Message
        self.for_album = for_album  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageLinkInfo":
        is_public = q.get('is_public')
        chat_id = q.get('chat_id')
        message = Object.read(q.get('message'))
        for_album = q.get('for_album')
        return MessageLinkInfo(is_public, chat_id, message, for_album)
