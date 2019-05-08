

from ..utils import Object


class OpenMessageContent(Object):
    """
    Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed 

    Attributes:
        ID (:obj:`str`): ``OpenMessageContent``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the message 
        message_id (:obj:`int`):
            Identifier of the message with the opened content

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "openMessageContent"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "OpenMessageContent":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return OpenMessageContent(chat_id, message_id)
