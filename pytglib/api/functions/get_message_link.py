

from ..utils import Object


class GetMessageLink(Object):
    """
    Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request

    Attributes:
        ID (:obj:`str`): ``GetMessageLink``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the message belongs
        message_id (:obj:`int`):
            Identifier of the message
        media_timestamp (:obj:`int`):
            If not 0, timestamp from which the video/audio/video note/voice note playing must start, in secondsThe media can be in the message content or in its web page preview
        for_album (:obj:`bool`):
            Pass true to create a link for the whole media album
        for_comment (:obj:`bool`):
            Pass true to create a link to the message as a channel post comment, or from a message thread

    Returns:
        MessageLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMessageLink"

    def __init__(self, chat_id, message_id, media_timestamp, for_album, for_comment, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.media_timestamp = media_timestamp  # int
        self.for_album = for_album  # bool
        self.for_comment = for_comment  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetMessageLink":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        media_timestamp = q.get('media_timestamp')
        for_album = q.get('for_album')
        for_comment = q.get('for_comment')
        return GetMessageLink(chat_id, message_id, media_timestamp, for_album, for_comment)
