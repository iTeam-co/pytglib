

from ..utils import Object


class AddChatToList(Object):
    """
    Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

    Attributes:
        ID (:obj:`str`): ``AddChatToList``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        chat_list (:class:`telegram.api.types.ChatList`):
            The chat listUse getChatListsToAddChat to get suitable chat lists

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addChatToList"

    def __init__(self, chat_id, chat_list, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.chat_list = chat_list  # ChatList

    @staticmethod
    def read(q: dict, *args) -> "AddChatToList":
        chat_id = q.get('chat_id')
        chat_list = Object.read(q.get('chat_list'))
        return AddChatToList(chat_id, chat_list)
