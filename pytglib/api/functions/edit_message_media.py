

from ..utils import Object


class EditMessageMedia(Object):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video. The media in the message can't be replaced if the message was set to self-destruct. Media can't be replaced by self-destructing media. Media in an album can be edited only to contain a photo or a video. Returns the edited message after the edit is completed on the server side

    Attributes:
        ID (:obj:`str`): ``EditMessageMedia``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; for bots only 
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            New content of the messageMust be one of the following types: InputMessageAnimation, InputMessageAudio, InputMessageDocument, InputMessagePhoto or InputMessageVideo

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageMedia"

    def __init__(self, chat_id, message_id, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "EditMessageMedia":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return EditMessageMedia(chat_id, message_id, reply_markup, input_message_content)
