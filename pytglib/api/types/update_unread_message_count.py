

from ..utils import Object


class UpdateUnreadMessageCount(Object):
    """
    Number of unread messages has changed. This update is sent only if a message database is used 

    Attributes:
        ID (:obj:`str`): ``UpdateUnreadMessageCount``

    Args:
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

    def __init__(self, unread_count, unread_unmuted_count, **kwargs):
        
        self.unread_count = unread_count  # int
        self.unread_unmuted_count = unread_unmuted_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateUnreadMessageCount":
        unread_count = q.get('unread_count')
        unread_unmuted_count = q.get('unread_unmuted_count')
        return UpdateUnreadMessageCount(unread_count, unread_unmuted_count)
