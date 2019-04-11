

from ..utils import Object


class EditInlineMessageCaption(Object):
    """
    Edits the caption of an inline message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``EditInlineMessageCaption``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup 
        caption (:class:`telegram.api.types.formattedText`):
            New message content caption; 0-GetOption("message_caption_length_max") characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageCaption"

    def __init__(self, inline_message_id, reply_markup, caption, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup
        self.caption = caption  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageCaption":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        caption = Object.read(q.get('caption'))
        return EditInlineMessageCaption(inline_message_id, reply_markup, caption)
