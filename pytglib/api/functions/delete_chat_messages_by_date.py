

from ..utils import Object


class DeleteChatMessagesByDate(Object):
    """
    Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted

    Attributes:
        ID (:obj:`str`): ``DeleteChatMessagesByDate``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        min_date (:obj:`int`):
            The minimum date of the messages to delete 
        max_date (:obj:`int`):
            The maximum date of the messages to delete 
        revoke (:obj:`bool`):
            Pass true to delete chat messages for all users; private chats only

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatMessagesByDate"

    def __init__(self, chat_id, min_date, max_date, revoke, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.min_date = min_date  # int
        self.max_date = max_date  # int
        self.revoke = revoke  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatMessagesByDate":
        chat_id = q.get('chat_id')
        min_date = q.get('min_date')
        max_date = q.get('max_date')
        revoke = q.get('revoke')
        return DeleteChatMessagesByDate(chat_id, min_date, max_date, revoke)
