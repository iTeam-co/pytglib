

from ..utils import Object


class ChatEventVideoChatMuteNewParticipantsToggled(Object):
    """
    The mute_new_participants setting of a video chat was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventVideoChatMuteNewParticipantsToggled``

    Args:
        mute_new_participants (:obj:`bool`):
            New value of the mute_new_participants setting

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventVideoChatMuteNewParticipantsToggled"

    def __init__(self, mute_new_participants, **kwargs):
        
        self.mute_new_participants = mute_new_participants  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventVideoChatMuteNewParticipantsToggled":
        mute_new_participants = q.get('mute_new_participants')
        return ChatEventVideoChatMuteNewParticipantsToggled(mute_new_participants)
