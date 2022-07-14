

from ..utils import Object


class AddLocalMessage(Object):
    """
    Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message

    Attributes:
        ID (:obj:`str`): ``AddLocalMessage``

    Args:
        chat_id (:obj:`int`):
            Target chat
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the sender of the message
        reply_to_message_id (:obj:`int`):
            Identifier of the replied message; 0 if none
        disable_notification (:obj:`bool`):
            Pass true to disable notification for the message
        input_message_content (:class:`telegram.api.types.InputMessageContent`):
            The content of the message to be added

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "addLocalMessage"

    def __init__(self, chat_id, sender_id, reply_to_message_id, disable_notification, input_message_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.sender_id = sender_id  # MessageSender
        self.reply_to_message_id = reply_to_message_id  # int
        self.disable_notification = disable_notification  # bool
        self.input_message_content = input_message_content  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "AddLocalMessage":
        chat_id = q.get('chat_id')
        sender_id = Object.read(q.get('sender_id'))
        reply_to_message_id = q.get('reply_to_message_id')
        disable_notification = q.get('disable_notification')
        input_message_content = Object.read(q.get('input_message_content'))
        return AddLocalMessage(chat_id, sender_id, reply_to_message_id, disable_notification, input_message_content)
