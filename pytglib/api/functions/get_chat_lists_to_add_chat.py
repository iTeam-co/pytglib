

from ..utils import Object


class GetChatListsToAddChat(Object):
    """
    Returns chat lists to which the chat can be added. This is an offline request 

    Attributes:
        ID (:obj:`str`): ``GetChatListsToAddChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        ChatLists

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatListsToAddChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatListsToAddChat":
        chat_id = q.get('chat_id')
        return GetChatListsToAddChat(chat_id)
