

from ..utils import Object


class DeleteChatHistory(Object):
    """
    Deletes all messages in the chat. Use Chat.can_be_deleted_only_for_self and Chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat

    Attributes:
        ID (:obj:`str`): ``DeleteChatHistory``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        remove_from_chat_list (:obj:`bool`):
            Pass true if the chat should be removed from the chat list 
        revoke (:obj:`bool`):
            Pass true to try to delete chat history for all users

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatHistory"

    def __init__(self, chat_id, remove_from_chat_list, revoke, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.remove_from_chat_list = remove_from_chat_list  # bool
        self.revoke = revoke  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatHistory":
        chat_id = q.get('chat_id')
        remove_from_chat_list = q.get('remove_from_chat_list')
        revoke = q.get('revoke')
        return DeleteChatHistory(chat_id, remove_from_chat_list, revoke)
