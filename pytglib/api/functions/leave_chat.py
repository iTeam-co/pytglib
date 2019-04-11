

from ..utils import Object


class LeaveChat(Object):
    """
    Removes current user from chat members. Private and secret chats can't be left using this method 

    Attributes:
        ID (:obj:`str`): ``LeaveChat``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "leaveChat"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "LeaveChat":
        chat_id = q.get('chat_id')
        return LeaveChat(chat_id)
