

from ..utils import Object


class GetVideoChatAvailableParticipants(Object):
    """
    Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined 

    Attributes:
        ID (:obj:`str`): ``GetVideoChatAvailableParticipants``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        MessageSenders

    Raises:
        :class:`telegram.Error`
    """
    ID = "getVideoChatAvailableParticipants"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetVideoChatAvailableParticipants":
        chat_id = q.get('chat_id')
        return GetVideoChatAvailableParticipants(chat_id)
