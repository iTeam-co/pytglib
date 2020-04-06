

from ..utils import Object


class UpdateUnreadMessageCount(Object):
    """
    Number of unread messages in a chat list has changed. This update is sent only if the message database is used 

    Attributes:
        ID (:obj:`str`): ``UpdateUnreadMessageCount``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            The chat list with changed number of unread messages
        unread_count (:obj:`int`):
            Total number of unread messages 
        unread_unmuted_count (:obj:`int`):
            Total number of unread messages in unmuted chats

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUnreadMessageCount"

    def __init__(self, chat_list, unread_count, unread_unmuted_count, **kwargs):
        
        self.chat_list = chat_list  # ChatList
        self.unread_count = unread_count  # int
        self.unread_unmuted_count = unread_unmuted_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateUnreadMessageCount":
        chat_list = Object.read(q.get('chat_list'))
        unread_count = q.get('unread_count')
        unread_unmuted_count = q.get('unread_unmuted_count')
        return UpdateUnreadMessageCount(chat_list, unread_count, unread_unmuted_count)
