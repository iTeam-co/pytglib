

from ..utils import Object


class StartGroupCallScreenSharing(Object):
    """
    Starts screen sharing in a joined group call. Returns join response payload for tgcalls

    Attributes:
        ID (:obj:`str`): ``StartGroupCallScreenSharing``

    Args:
        group_call_id (:obj:`int`):
            Group call identifier
        audio_source_id (:obj:`int`):
            Screen sharing audio channel synchronization source identifier; received from tgcalls
        payload (:obj:`str`):
            Group call join payload; received from tgcalls

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "startGroupCallScreenSharing"

    def __init__(self, group_call_id, audio_source_id, payload, extra=None, **kwargs):
        self.extra = extra
        self.group_call_id = group_call_id  # int
        self.audio_source_id = audio_source_id  # int
        self.payload = payload  # str

    @staticmethod
    def read(q: dict, *args) -> "StartGroupCallScreenSharing":
        group_call_id = q.get('group_call_id')
        audio_source_id = q.get('audio_source_id')
        payload = q.get('payload')
        return StartGroupCallScreenSharing(group_call_id, audio_source_id, payload)
