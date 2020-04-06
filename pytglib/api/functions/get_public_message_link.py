

from ..utils import Object


class GetPublicMessageLink(Object):
    """
    Returns a public HTTPS link to a message. Available only for messages in supergroups and channels with a username

    Attributes:
        ID (:obj:`str`): ``GetPublicMessageLink``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message
        for_album (:obj:`bool`):
            Pass true if a link for a whole media album should be returned

    Returns:
        PublicMessageLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPublicMessageLink"

    def __init__(self, chat_id, message_id, for_album, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.for_album = for_album  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetPublicMessageLink":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        for_album = q.get('for_album')
        return GetPublicMessageLink(chat_id, message_id, for_album)
