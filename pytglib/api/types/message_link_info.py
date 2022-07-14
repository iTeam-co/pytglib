

from ..utils import Object


class MessageLinkInfo(Object):
    """
    Contains information about a link to a message in a chat

    Attributes:
        ID (:obj:`str`): ``MessageLinkInfo``

    Args:
        is_public (:obj:`bool`):
            True, if the link is a public link for a message in a chat
        chat_id (:obj:`int`):
            If found, identifier of the chat to which the message belongs, 0 otherwise
        message (:class:`telegram.api.types.message`):
            If found, the linked message; may be null
        media_timestamp (:obj:`int`):
            Timestamp from which the video/audio/video note/voice note playing must start, in seconds; 0 if not specifiedThe media can be in the message content or in its web page preview
        for_album (:obj:`bool`):
            True, if the whole media album to which the message belongs is linked
        for_comment (:obj:`bool`):
            True, if the message is linked as a channel post comment or from a message thread

    Returns:
        MessageLinkInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageLinkInfo"

    def __init__(self, is_public, chat_id, message, media_timestamp, for_album, for_comment, **kwargs):
        
        self.is_public = is_public  # bool
        self.chat_id = chat_id  # int
        self.message = message  # Message
        self.media_timestamp = media_timestamp  # int
        self.for_album = for_album  # bool
        self.for_comment = for_comment  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageLinkInfo":
        is_public = q.get('is_public')
        chat_id = q.get('chat_id')
        message = Object.read(q.get('message'))
        media_timestamp = q.get('media_timestamp')
        for_album = q.get('for_album')
        for_comment = q.get('for_comment')
        return MessageLinkInfo(is_public, chat_id, message, media_timestamp, for_album, for_comment)
