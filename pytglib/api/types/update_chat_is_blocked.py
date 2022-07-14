

from ..utils import Object


class UpdateChatIsBlocked(Object):
    """
    A chat was blocked or unblocked 

    Attributes:
        ID (:obj:`str`): ``UpdateChatIsBlocked``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_blocked (:obj:`bool`):
            New value of is_blocked

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatIsBlocked"

    def __init__(self, chat_id, is_blocked, **kwargs):
        
        self.chat_id = chat_id  # int
        self.is_blocked = is_blocked  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatIsBlocked":
        chat_id = q.get('chat_id')
        is_blocked = q.get('is_blocked')
        return UpdateChatIsBlocked(chat_id, is_blocked)
