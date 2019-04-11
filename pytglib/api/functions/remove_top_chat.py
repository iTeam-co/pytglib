

from ..utils import Object


class RemoveTopChat(Object):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled 

    Attributes:
        ID (:obj:`str`): ``RemoveTopChat``

    Args:
        category (:class:`telegram.api.types.TopChatCategory`):
            Category of frequently used chats 
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeTopChat"

    def __init__(self, category, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.category = category  # TopChatCategory
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RemoveTopChat":
        category = Object.read(q.get('category'))
        chat_id = q.get('chat_id')
        return RemoveTopChat(category, chat_id)
