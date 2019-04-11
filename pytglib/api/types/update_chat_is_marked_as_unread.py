

from ..utils import Object


class UpdateChatIsMarkedAsUnread(Object):
    """
    A chat was marked as unread or was read 

    Attributes:
        ID (:obj:`str`): ``UpdateChatIsMarkedAsUnread``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_marked_as_unread (:obj:`bool`):
            New value of is_marked_as_unread

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatIsMarkedAsUnread"

    def __init__(self, chat_id, is_marked_as_unread, **kwargs):
        
        self.chat_id = chat_id  # int
        self.is_marked_as_unread = is_marked_as_unread  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatIsMarkedAsUnread":
        chat_id = q.get('chat_id')
        is_marked_as_unread = q.get('is_marked_as_unread')
        return UpdateChatIsMarkedAsUnread(chat_id, is_marked_as_unread)
