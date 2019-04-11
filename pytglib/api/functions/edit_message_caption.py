

from ..utils import Object


class EditMessageCaption(Object):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side

    Attributes:
        ID (:obj:`str`): ``EditMessageCaption``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; for bots only 
        caption (:class:`telegram.api.types.formattedText`):
            New message content caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageCaption"

    def __init__(self, chat_id, message_id, reply_markup, caption, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "EditMessageCaption":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        caption = Object.read(q.get('caption'))
        return EditMessageCaption(chat_id, message_id, reply_markup, caption)
