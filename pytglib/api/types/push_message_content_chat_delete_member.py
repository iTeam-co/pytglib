

from ..utils import Object


class PushMessageContentChatDeleteMember(Object):
    """
    A chat member was deleted 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentChatDeleteMember``

    Args:
        member_name (:obj:`str`):
            Name of the deleted member 
        is_current_user (:obj:`bool`):
            True, if the current user was deleted from the group
        is_left (:obj:`bool`):
            True, if the user has left the group themself

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentChatDeleteMember"

    def __init__(self, member_name, is_current_user, is_left, **kwargs):
        
        self.member_name = member_name  # str
        self.is_current_user = is_current_user  # bool
        self.is_left = is_left  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentChatDeleteMember":
        member_name = q.get('member_name')
        is_current_user = q.get('is_current_user')
        is_left = q.get('is_left')
        return PushMessageContentChatDeleteMember(member_name, is_current_user, is_left)
