

from ..utils import Object


class SetChatChatList(Object):
    """
    Moves a chat to a different chat list. Current chat list of the chat must ne non-null 

    Attributes:
        ID (:obj:`str`): ``SetChatChatList``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        chat_list (:class:`telegram.api.types.ChatList`):
            New chat list of the chatThe chat with the current user (Saved Messages) and the chat 777000 (Telegram) can't be moved to the Archive chat list

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatChatList"

    def __init__(self, chat_id, chat_list, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.chat_list = chat_list  # ChatList

    @staticmethod
    def read(q: dict, *args) -> "SetChatChatList":
        chat_id = q.get('chat_id')
        chat_list = Object.read(q.get('chat_list'))
        return SetChatChatList(chat_id, chat_list)
