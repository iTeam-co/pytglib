

from ..utils import Object


class PushMessageContentChatAddMembers(Object):
    """
    New chat members were invited to a group 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatAddMembers``

    Args:
        member_name (:obj:`str`):
            Name of the added member 
        is_current_user (:obj:`bool`):
            True, if the current user was added to the group
        is_returned (:obj:`bool`):
            True, if the user has returned to the group themself

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatAddMembers"

    def __init__(self, member_name, is_current_user, is_returned, **kwargs):
        
        self.member_name = member_name  # str
        self.is_current_user = is_current_user  # bool
        self.is_returned = is_returned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatAddMembers":
        member_name = q.get('member_name')
        is_current_user = q.get('is_current_user')
        is_returned = q.get('is_returned')
        return PushMessageContentChatAddMembers(member_name, is_current_user, is_returned)
