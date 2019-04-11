

from ..utils import Object


class EditMessageText(Object):
    """
    Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side

    Attributes:
        ID (:obj:`str`): ``EditMessageText``

    Args:
        chat_id (:obj:`int`):
            The chat the message belongs to 
        message_id (:obj:`int`):
            Identifier of the message 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; for bots only 
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            New text content of the messageShould be of type InputMessageText

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "editMessageText"

    def __init__(self, chat_id, message_id, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "EditMessageText":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return EditMessageText(chat_id, message_id, reply_markup, input_message_content)
