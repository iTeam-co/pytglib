

from ..utils import Object


class SendMessageAlbum(Object):
    """
    Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

    Attributes:
        ID (:obj:`str`): ``SendMessageAlbum``

    Args:
        chat_id (:obj:`int`):
            Target chat
        message_thread_id (:obj:`int`):
            If not 0, a message thread identifier in which the messages will be sent
        reply_to_message_id (:obj:`int`):
            Identifier of a replied message; 0 if none
        options (:class:`telegram.api.types.messageSendOptions`):
            Options to be used to send the messages; pass null to use default options
        input_message_contents (List of :class:`telegram.api.types.InputMessageContent`):
            Contents of messages to be sentAt most 10 messages can be added to an album
        only_preview (:obj:`bool`):
            Pass true to get fake messages instead of actually sending them

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessageAlbum"

    def __init__(self, chat_id, message_thread_id, reply_to_message_id, options, input_message_contents, only_preview, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.options = options  # MessageSendOptions
        self.input_message_contents = input_message_contents  # list of InputMessageContent
        self.only_preview = only_preview  # bool

    @staticmethod
    def read(q: dict, *args) -> "SendMessageAlbum":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        reply_to_message_id = q.get('reply_to_message_id')
        options = Object.read(q.get('options'))
        input_message_contents = [Object.read(i) for i in q.get('input_message_contents', [])]
        only_preview = q.get('only_preview')
        return SendMessageAlbum(chat_id, message_thread_id, reply_to_message_id, options, input_message_contents, only_preview)
