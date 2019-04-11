

from ..utils import Object


class EditInlineMessageText(Object):
    """
    Edits the text of an inline text or game message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``EditInlineMessageText``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup 
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            New text content of the messageShould be of type InputMessageText

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageText"

    def __init__(self, inline_message_id, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageText":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return EditInlineMessageText(inline_message_id, reply_markup, input_message_content)
