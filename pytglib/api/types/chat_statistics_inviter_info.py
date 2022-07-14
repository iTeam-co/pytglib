

from ..utils import Object


class ChatStatisticsInviterInfo(Object):
    """
    Contains statistics about number of new members invited by a user

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsInviterInfo``

    Args:
        user_id (:obj:`int`):
            User identifier
        added_member_count (:obj:`int`):
            Number of new members invited by the user

    Returns:
        ChatStatisticsInviterInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsInviterInfo"

    def __init__(self, user_id, added_member_count, **kwargs):
        
        self.user_id = user_id  # int
        self.added_member_count = added_member_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsInviterInfo":
        user_id = q.get('user_id')
        added_member_count = q.get('added_member_count')
        return ChatStatisticsInviterInfo(user_id, added_member_count)
