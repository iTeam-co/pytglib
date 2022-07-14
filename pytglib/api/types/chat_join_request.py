

from ..utils import Object


class ChatJoinRequest(Object):
    """
    Describes a user that sent a join request and waits for administrator approval 

    Attributes:
        ID (:obj:`str`): ``ChatJoinRequest``

    Args:
        user_id (:obj:`int`):
            User identifier 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the user sent the join request 
        bio (:obj:`str`):
            A short bio of the user

    Returns:
        ChatJoinRequest

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatJoinRequest"

    def __init__(self, user_id, date, bio, **kwargs):
        
        self.user_id = user_id  # int
        self.date = date  # int
        self.bio = bio  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatJoinRequest":
        user_id = q.get('user_id')
        date = q.get('date')
        bio = q.get('bio')
        return ChatJoinRequest(user_id, date, bio)
