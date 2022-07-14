

from ..utils import Object


class RevokeGroupCallInviteLink(Object):
    """
    Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag 

    Attributes:
        ID (:obj:`str`): ``RevokeGroupCallInviteLink``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "revokeGroupCallInviteLink"

    def __init__(self, group_call_id, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int

    @staticmethod
    def read(q: dict, *args) -> "RevokeGroupCallInviteLink":
        group_call_id = q.get('group_call_id')
        return RevokeGroupCallInviteLink(group_call_id)
