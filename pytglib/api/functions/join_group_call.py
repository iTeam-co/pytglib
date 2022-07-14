

from ..utils import Object


class JoinGroupCall(Object):
    """
    Joins an active group call. Returns join response payload for tgcalls

    Attributes:
        ID (:obj:`str`): ``JoinGroupCall``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier
        participant_id (:class:`telegram.api.types.MessageSender`):
            Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only
        audio_source_id (:obj:`int`):
            Caller audio channel synchronization source identifier; received from tgcalls
        payload (:obj:`str`):
            Group call join payload; received from tgcalls
        is_muted (:obj:`bool`):
            Pass true to join the call with muted microphone
        is_my_video_enabled (:obj:`bool`):
            Pass true if the user's video is enabled
        invite_hash (:obj:`str`):
            If non-empty, invite hash to be used to join the group call without being muted by administrators

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "joinGroupCall"

    def __init__(self, group_call_id, participant_id, audio_source_id, payload, is_muted, is_my_video_enabled, invite_hash, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.participant_id = participant_id  # MessageSender
        self.audio_source_id = audio_source_id  # int
        self.payload = payload  # str
        self.is_muted = is_muted  # bool
        self.is_my_video_enabled = is_my_video_enabled  # bool
        self.invite_hash = invite_hash  # str

    @staticmethod
    def read(q: dict, *args) -> "JoinGroupCall":
        group_call_id = q.get('group_call_id')
        participant_id = Object.read(q.get('participant_id'))
        audio_source_id = q.get('audio_source_id')
        payload = q.get('payload')
        is_muted = q.get('is_muted')
        is_my_video_enabled = q.get('is_my_video_enabled')
        invite_hash = q.get('invite_hash')
        return JoinGroupCall(group_call_id, participant_id, audio_source_id, payload, is_muted, is_my_video_enabled, invite_hash)
