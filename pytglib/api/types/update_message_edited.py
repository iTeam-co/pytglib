

from ..utils import Object


class UpdateMessageEdited(Object):
    """
    A message was edited. Changes in the message content will come in a separate updateMessageContent 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageEdited``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        edit_date (:obj:`int`):
            Point in time (Unix timestamp) when the message was edited 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            New message reply markup; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageEdited"

    def __init__(self, chat_id, message_id, edit_date, reply_markup, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.edit_date = edit_date  # int
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageEdited":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        edit_date = q.get('edit_date')
        reply_markup = Object.read(q.get('reply_markup'))
        return UpdateMessageEdited(chat_id, message_id, edit_date, reply_markup)
