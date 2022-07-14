

from ..utils import Object


class MessageInviteVideoChatParticipants(Object):
    """
    A message with information about an invite to a video chat 

    Attributes:
        ID (:obj:`str`): ``MessageInviteVideoChatParticipants``

    Args:
        group_call_id (:obj:`int`):
            Identifier of the video chatThe video chat can be received through the method getGroupCall 
        user_ids (List of :obj:`int`):
            Invited user identifiers

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageInviteVideoChatParticipants"

    def __init__(self, group_call_id, user_ids, **kwargs):
        
        self.group_call_id = group_call_id  # int
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "MessageInviteVideoChatParticipants":
        group_call_id = q.get('group_call_id')
        user_ids = q.get('user_ids')
        return MessageInviteVideoChatParticipants(group_call_id, user_ids)
