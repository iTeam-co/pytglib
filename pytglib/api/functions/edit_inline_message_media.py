

from ..utils import Object


class EditInlineMessageMedia(Object):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only 

    Attributes:
        ID (:obj:`str`): ``EditInlineMessageMedia``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; for bots only 
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            New content of the messageMust be one of the following types: InputMessageAnimation, InputMessageAudio, InputMessageDocument, InputMessagePhoto or InputMessageVideo

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "editInlineMessageMedia"

    def __init__(self, inline_message_id, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "EditInlineMessageMedia":
        inline_message_id = q.get('inline_message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return EditInlineMessageMedia(inline_message_id, reply_markup, input_message_content)
