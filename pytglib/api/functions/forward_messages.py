

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
        options (:class:`telegram.api.types.sendMessageOptions`):
            Options to be used to send the messages
        as_album (:obj:`bool`):
            True, if the messages should be grouped into an album after forwardingFor this to work, no more than 10 messages may be forwarded, and all of them must be photo or video messages
        send_copy (:obj:`bool`):
            True, if content of the messages needs to be copied without links to the original messagesAlways true if the messages are forwarded to a secret chat
        remove_caption (:obj:`bool`):
            True, if media captions of message copies needs to be removedIgnored if send_copy is false

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "forwardMessages"

    def __init__(self, chat_id, from_chat_id, message_ids, options, as_album, send_copy, remove_caption, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.from_chat_id = from_chat_id  # int
        self.message_ids = message_ids  # list of int
        self.options = options  # SendMessageOptions
        self.as_album = as_album  # bool
        self.send_copy = send_copy  # bool
        self.remove_caption = remove_caption  # bool

    @staticmethod
    def read(q: dict, *args) -> "ForwardMessages":
        chat_id = q.get('chat_id')
        from_chat_id = q.get('from_chat_id')
        message_ids = q.get('message_ids')
        options = Object.read(q.get('options'))
        as_album = q.get('as_album')
        send_copy = q.get('send_copy')
        remove_caption = q.get('remove_caption')
        return ForwardMessages(chat_id, from_chat_id, message_ids, options, as_album, send_copy, remove_caption)
