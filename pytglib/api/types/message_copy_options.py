

from ..utils import Object


class MessageCopyOptions(Object):
    """
    Options to be used when a message content is copied without reference to the original sender. Service messages and messageInvoice can't be copied

    Attributes:
        ID (:obj:`str`): ``MessageCopyOptions``

    Args:
        send_copy (:obj:`bool`):
            True, if content of the message needs to be copied without reference to the original senderAlways true if the message is forwarded to a secret chat or is local
        replace_caption (:obj:`bool`):
            True, if media caption of the message copy needs to be replacedIgnored if send_copy is false
        new_caption (:class:`telegram.api.types.formattedText`):
            New message caption; pass null to copy message without captionIgnored if replace_caption is false

    Returns:
        MessageCopyOptions

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageCopyOptions"

    def __init__(self, send_copy, replace_caption, new_caption, **kwargs):
        
        self.send_copy = send_copy  # bool
        self.replace_caption = replace_caption  # bool
        self.new_caption = new_caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "MessageCopyOptions":
        send_copy = q.get('send_copy')
        replace_caption = q.get('replace_caption')
        new_caption = Object.read(q.get('new_caption'))
        return MessageCopyOptions(send_copy, replace_caption, new_caption)
