

from ..utils import Object


class EditInlineMessageReplyMarkup(Object):
    """
    Edits the reply markup of an inline message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``EditInlineMessageReplyMarkup``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageReplyMarkup"

    def __init__(self, inline_message_id, reply_markup, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageReplyMarkup":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        return EditInlineMessageReplyMarkup(inline_message_id, reply_markup)
