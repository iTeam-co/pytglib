

from ..utils import Object


class UpdateUnreadChatCount(Object):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if a message database is used

    Attributes:
        ID (:obj:`str`): ``UpdateUnreadChatCount``

    Args:
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

    def __init__(self, unread_count, unread_unmuted_count, marked_as_unread_count, marked_as_unread_unmuted_count, **kwargs):
        
        self.unread_count = unread_count  # int
        self.unread_unmuted_count = unread_unmuted_count  # int
        self.marked_as_unread_count = marked_as_unread_count  # int
        self.marked_as_unread_unmuted_count = marked_as_unread_unmuted_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateUnreadChatCount":
        unread_count = q.get('unread_count')
        unread_unmuted_count = q.get('unread_unmuted_count')
        marked_as_unread_count = q.get('marked_as_unread_count')
        marked_as_unread_unmuted_count = q.get('marked_as_unread_unmuted_count')
        return UpdateUnreadChatCount(unread_count, unread_unmuted_count, marked_as_unread_count, marked_as_unread_unmuted_count)
