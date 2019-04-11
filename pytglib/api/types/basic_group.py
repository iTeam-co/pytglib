

from ..utils import Object


class BasicGroup(Object):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)

    Attributes:
        ID (:obj:`str`): ``BasicGroup``

    Args:
        id (:obj:`int`):
            Group identifier
        member_count (:obj:`int`):
            Number of members in the group
        status (:class:`telegram.api.types.ChatMemberStatus`):
            Status of the current user in the group
        everyone_is_administrator (:obj:`bool`):
            True, if all members have been granted administrator rights in the group
        is_active (:obj:`bool`):
            True, if the group is active
        upgraded_to_supergroup_id (:obj:`int`):
            Identifier of the supergroup to which this group was upgraded; 0 if none

    Returns:
        BasicGroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "basicGroup"

    def __init__(self, id, member_count, status, everyone_is_administrator, is_active, upgraded_to_supergroup_id, **kwargs):
        
        self.id = id  # int
        self.member_count = member_count  # int
        self.status = status  # ChatMemberStatus
        self.everyone_is_administrator = everyone_is_administrator  # bool
        self.is_active = is_active  # bool
        self.upgraded_to_supergroup_id = upgraded_to_supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "BasicGroup":
        id = q.get('id')
        member_count = q.get('member_count')
        status = Object.read(q.get('status'))
        everyone_is_administrator = q.get('everyone_is_administrator')
        is_active = q.get('is_active')
        upgraded_to_supergroup_id = q.get('upgraded_to_supergroup_id')
        return BasicGroup(id, member_count, status, everyone_is_administrator, is_active, upgraded_to_supergroup_id)
