

from ..utils import Object


class GetMessageEmbeddingCode(Object):
    """
    Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username

    Attributes:
        ID (:obj:`str`): ``GetMessageEmbeddingCode``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message
        for_album (:obj:`bool`):
            Pass true to return an HTML code for embedding of the whole media album

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageEmbeddingCode"

    def __init__(self, chat_id, message_id, for_album, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.for_album = for_album  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetMessageEmbeddingCode":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        for_album = q.get('for_album')
        return GetMessageEmbeddingCode(chat_id, message_id, for_album)
