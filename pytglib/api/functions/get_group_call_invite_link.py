

from ..utils import Object


class GetGroupCallInviteLink(Object):
    """
    Returns invite link to a video chat in a public chat

    Attributes:
        ID (:obj:`str`): ``GetGroupCallInviteLink``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier
        can_self_unmute (:obj:`bool`):
            Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselvesRequires groupCallcan_be_managed group call flag

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGroupCallInviteLink"

    def __init__(self, group_call_id, can_self_unmute, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.can_self_unmute = can_self_unmute  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetGroupCallInviteLink":
        group_call_id = q.get('group_call_id')
        can_self_unmute = q.get('can_self_unmute')
        return GetGroupCallInviteLink(group_call_id, can_self_unmute)
