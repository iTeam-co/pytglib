

from ..utils import Object


class UpdateUnreadChatCount(Object):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if the message database is used

    Attributes:
        ID (:obj:`str`): ``UpdateUnreadChatCount``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            The chat list with changed number of unread messages
        total_count (:obj:`int`):
            Approximate total number of chats in the chat list
        unread_count (:obj:`int`):
            Total number of unread chats 
        unread_unmuted_count (:obj:`int`):
            Total number of unread unmuted chats
        marked_as_unread_count (:obj:`int`):
            Total number of chats marked as unread 
        marked_as_unread_unmuted_count (:obj:`int`):
            Total number of unmuted chats marked as unread

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateUnreadChatCount"

    def __init__(self, chat_list, total_count, unread_count, unread_unmuted_count, marked_as_unread_count, marked_as_unread_unmuted_count, **kwargs):
        
        self.chat_list = chat_list  # ChatList
        self.total_count = total_count  # int
        self.unread_count = unread_count  # int
        self.unread_unmuted_count = unread_unmuted_count  # int
        self.marked_as_unread_count = marked_as_unread_count  # int
        self.marked_as_unread_unmuted_count = marked_as_unread_unmuted_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateUnreadChatCount":
        chat_list = Object.read(q.get('chat_list'))
        total_count = q.get('total_count')
        unread_count = q.get('unread_count')
        unread_unmuted_count = q.get('unread_unmuted_count')
        marked_as_unread_count = q.get('marked_as_unread_count')
        marked_as_unread_unmuted_count = q.get('marked_as_unread_unmuted_count')
        return UpdateUnreadChatCount(chat_list, total_count, unread_count, unread_unmuted_count, marked_as_unread_count, marked_as_unread_unmuted_count)
