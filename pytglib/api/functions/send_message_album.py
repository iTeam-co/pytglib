

from ..utils import Object


class SendMessageAlbum(Object):
    """
    Sends messages grouped together into an album. Currently only photo and video messages can be grouped into an album. Returns sent messages

    Attributes:
        ID (:obj:`str`): ``SendMessageAlbum``

    Args:
        chat_id (:obj:`int`):
            Target chat 
        reply_to_message_id (:obj:`int`):
            Identifier of a message to reply to or 0
        options (:class:`telegram.api.types.sendMessageOptions`):
            Options to be used to send the messages
        input_message_contents (List of :class:`telegram.api.types.InputMessageContent`):
            Contents of messages to be sent

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessageAlbum"

    def __init__(self, chat_id, reply_to_message_id, options, input_message_contents, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.options = options  # SendMessageOptions
        self.input_message_contents = input_message_contents  # list of InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "SendMessageAlbum":
        chat_id = q.get('chat_id')
        reply_to_message_id = q.get('reply_to_message_id')
        options = Object.read(q.get('options'))
        input_message_contents = [Object.read(i) for i in q.get('input_message_contents', [])]
        return SendMessageAlbum(chat_id, reply_to_message_id, options, input_message_contents)
