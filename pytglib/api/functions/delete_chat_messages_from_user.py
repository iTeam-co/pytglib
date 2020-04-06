

from ..utils import Object


class DeleteChatMessagesFromUser(Object):
    """
    Deletes all messages sent by the specified user to a chat. Supported only for supergroups; requires can_delete_messages administrator privileges 

    Attributes:
        ID (:obj:`str`): ``DeleteChatMessagesFromUser``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            User identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatMessagesFromUser"

    def __init__(self, chat_id, user_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatMessagesFromUser":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        return DeleteChatMessagesFromUser(chat_id, user_id)
