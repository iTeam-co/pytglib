

from ..utils import Object


class InternalLinkTypeVideoChat(Object):
    """
    The link is a link to a video chat. Call searchPublicChat with the given chat username, and then joinGroupCall with the given invite hash to process the link

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeVideoChat``

    Args:
        chat_username (:obj:`str`):
            Username of the chat with the video chat 
        invite_hash (:obj:`str`):
            If non-empty, invite hash to be used to join the video chat without being muted by administrators
        is_live_stream (:obj:`bool`):
            True, if the video chat is expected to be a live stream in a channel or a broadcast group

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeVideoChat"

    def __init__(self, chat_username, invite_hash, is_live_stream, **kwargs):
        
        self.chat_username = chat_username  # str
        self.invite_hash = invite_hash  # str
        self.is_live_stream = is_live_stream  # bool

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeVideoChat":
        chat_username = q.get('chat_username')
        invite_hash = q.get('invite_hash')
        is_live_stream = q.get('is_live_stream')
        return InternalLinkTypeVideoChat(chat_username, invite_hash, is_live_stream)
