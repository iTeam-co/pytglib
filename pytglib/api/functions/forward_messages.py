

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
            Identifiers of the messages to forwardMessage identifiers must be in a strictly increasing orderAt most 100 messages can be forwarded simultaneously
        options (:class:`telegram.api.types.messageSendOptions`):
            Options to be used to send the messages; pass null to use default options
        send_copy (:obj:`bool`):
            Pass true to copy content of the messages without reference to the original senderAlways true if the messages are forwarded to a secret chat or are local
        remove_caption (:obj:`bool`):
            Pass true to remove media captions of message copiesIgnored if send_copy is false
        only_preview (:obj:`bool`):
            Pass true to get fake messages instead of actually forwarding them

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "forwardMessages"

    def __init__(self, chat_id, from_chat_id, message_ids, options, send_copy, remove_caption, only_preview, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.from_chat_id = from_chat_id  # int
        self.message_ids = message_ids  # list of int
        self.options = options  # MessageSendOptions
        self.send_copy = send_copy  # bool
        self.remove_caption = remove_caption  # bool
        self.only_preview = only_preview  # bool

    @staticmethod
    def read(q: dict, *args) -> "ForwardMessages":
        chat_id = q.get('chat_id')
        from_chat_id = q.get('from_chat_id')
        message_ids = q.get('message_ids')
        options = Object.read(q.get('options'))
        send_copy = q.get('send_copy')
        remove_caption = q.get('remove_caption')
        only_preview = q.get('only_preview')
        return ForwardMessages(chat_id, from_chat_id, message_ids, options, send_copy, remove_caption, only_preview)
