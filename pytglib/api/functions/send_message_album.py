

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
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the messagesNot supported in secret chats 
        from_background (:obj:`bool`):
            Pass true if the messages are sent from the background
        input_message_contents (List of :class:`telegram.api.types.InputMessageContent`):
            Contents of messages to be sent

    Returns:
        Messages

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendMessageAlbum"

    def __init__(self, chat_id, reply_to_message_id, disable_notification, from_background, input_message_contents, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.reply_to_message_id = reply_to_message_id  # int
        self.disable_notification = disable_notification  # bool
        self.from_background = from_background  # bool
        self.input_message_contents = input_message_contents  # list of InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "SendMessageAlbum":
        chat_id = q.get('chat_id')
        reply_to_message_id = q.get('reply_to_message_id')
        disable_notification = q.get('disable_notification')
        from_background = q.get('from_background')
        input_message_contents = [Object.read(i) for i in q.get('input_message_contents', [])]
        return SendMessageAlbum(chat_id, reply_to_message_id, disable_notification, from_background, input_message_contents)
