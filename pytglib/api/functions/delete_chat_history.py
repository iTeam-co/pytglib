

from ..utils import Object


class DeleteChatHistory(Object):
    """
    Deletes all messages in the chat only for the user. Cannot be used in channels and public supergroups 

    Attributes:
        ID (:obj:`str`): ``DeleteChatHistory``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        remove_from_chat_list (:obj:`bool`):
            Pass true if the chat should be removed from the chats list

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatHistory"

    def __init__(self, chat_id, remove_from_chat_list, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.remove_from_chat_list = remove_from_chat_list  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatHistory":
        chat_id = q.get('chat_id')
        remove_from_chat_list = q.get('remove_from_chat_list')
        return DeleteChatHistory(chat_id, remove_from_chat_list)
