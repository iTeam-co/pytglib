

from ..utils import Object


class ToggleChatIsMarkedAsUnread(Object):
    """
    Changes the marked as unread state of a chat 

    Attributes:
        ID (:obj:`str`): ``ToggleChatIsMarkedAsUnread``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_marked_as_unread (:obj:`bool`):
            New value of is_marked_as_unread

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleChatIsMarkedAsUnread"

    def __init__(self, chat_id, is_marked_as_unread, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.is_marked_as_unread = is_marked_as_unread  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleChatIsMarkedAsUnread":
        chat_id = q.get('chat_id')
        is_marked_as_unread = q.get('is_marked_as_unread')
        return ToggleChatIsMarkedAsUnread(chat_id, is_marked_as_unread)
