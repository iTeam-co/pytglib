

from ..utils import Object


class GetMessageLink(Object):
    """
    Returns a private HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels. The link will work only for members of the chat

    Attributes:
        ID (:obj:`str`): ``GetMessageLink``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageLink"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMessageLink":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetMessageLink(chat_id, message_id)
