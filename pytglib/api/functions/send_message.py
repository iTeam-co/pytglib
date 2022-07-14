

from ..utils import Object


class SendMessage(Object):
    """
    Sends a message. Returns the sent message

    Attributes:
        ID (:obj:`str`): ``SendMessage``

    Args:
        chat_id (:obj:`int`):
            Target chat
        message_thread_id (:obj:`int`):
            If not 0, a message thread identifier in which the message will be sent
        reply_to_message_id (:obj:`int`):
            Identifier of the replied message; 0 if none
        options (:class:`telegram.api.types.messageSendOptions`):
            Options to be used to send the message; pass null to use default options
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            Markup for replying to the message; pass null if none; for bots only
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be sent

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessage"

    def __init__(self, chat_id, message_thread_id, reply_to_message_id, options, reply_markup, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.options = options  # MessageSendOptions
        self.reply_markup = reply_markup  # ReplyMarkup
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "SendMessage":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        reply_to_message_id = q.get('reply_to_message_id')
        options = Object.read(q.get('options'))
        reply_markup = Object.read(q.get('reply_markup'))
        input_message_content = Object.read(q.get('input_message_content'))
        return SendMessage(chat_id, message_thread_id, reply_to_message_id, options, reply_markup, input_message_content)
