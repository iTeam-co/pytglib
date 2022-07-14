

from ..utils import Object


class InviteGroupCallParticipants(Object):
    """
    Invites users to an active group call. Sends a service message of type messageInviteToGroupCall for video chats

    Attributes:
        ID (:obj:`str`): ``InviteGroupCallParticipants``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier 
        user_ids (List of :obj:`int`):
            User identifiersAt most 10 users can be invited simultaneously

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "inviteGroupCallParticipants"

    def __init__(self, group_call_id, user_ids, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "InviteGroupCallParticipants":
        group_call_id = q.get('group_call_id')
        user_ids = q.get('user_ids')
        return InviteGroupCallParticipants(group_call_id, user_ids)
