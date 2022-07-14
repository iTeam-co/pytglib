

from ..utils import Object


class SetVideoChatDefaultParticipant(Object):
    """
    Changes default participant identifier, on whose behalf a video chat in the chat will be joined 

    Attributes:
        ID (:obj:`str`): ``SetVideoChatDefaultParticipant``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        default_participant_id (:class:`telegram.api.types.MessageSender`):
            Default group call participant identifier to join the video chats

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setVideoChatDefaultParticipant"

    def __init__(self, chat_id, default_participant_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.default_participant_id = default_participant_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "SetVideoChatDefaultParticipant":
        chat_id = q.get('chat_id')
        default_participant_id = Object.read(q.get('default_participant_id'))
        return SetVideoChatDefaultParticipant(chat_id, default_participant_id)
