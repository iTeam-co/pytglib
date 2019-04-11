

from ..utils import Object


class ForwardMessages(Object):
    """
    Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message

    Attributes:
        ID (:obj:`str`): ``ForwardMessages``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which to forward messages 
        from_chat_id (:obj:`int`):
            Identifier of the chat from which to forward messages 
        message_ids (List of :obj:`int`):
            Identifiers of the messages to forward
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the message, doesn't work if messages are forwarded to a secret chat 
        from_background (:obj:`bool`):
            Pass true if the message is sent from the background
        as_album (:obj:`bool`):
            True, if the messages should be grouped into an album after forwardingFor this to work, no more than 10 messages may be forwarded, and all of them must be photo or video messages

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "forwardMessages"

    def __init__(self, chat_id, from_chat_id, message_ids, disable_notification, from_background, as_album, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.from_chat_id = from_chat_id  # int
        self.message_ids = message_ids  # list of int
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.as_album = as_album  # bool

    @staticmethod
    def read(q: dict, *args) -> "ForwardMessages":
        chat_id = q.get('chat_id')
        from_chat_id = q.get('from_chat_id')
        message_ids = q.get('message_ids')
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        as_album = q.get('as_album')
        return ForwardMessages(chat_id, from_chat_id, message_ids, disable_notification, from_background, as_album)
