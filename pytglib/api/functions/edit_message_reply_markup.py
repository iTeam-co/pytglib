

from ..utils import Object


class EditMessageReplyMarkup(Object):
    """
    Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side

    Attributes:
        ID (:obj:`str`): ``EditMessageReplyMarkup``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageReplyMarkup"

    def __init__(self, chat_id, message_id, reply_markup, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "EditMessageReplyMarkup":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        return EditMessageReplyMarkup(chat_id, message_id, reply_markup)
