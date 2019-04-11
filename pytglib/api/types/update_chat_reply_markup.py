

from ..utils import Object


class UpdateChatReplyMarkup(Object):
    """
    The default chat reply markup was changed. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user

    Attributes:
        ID (:obj:`str`): ``UpdateChatReplyMarkup``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        reply_markup_message_id (:obj:`int`):
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatReplyMarkup"

    def __init__(self, chat_id, reply_markup_message_id, **kwargs):
        
        self.chat_id = chat_id  # int
        self.reply_markup_message_id = reply_markup_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatReplyMarkup":
        chat_id = q.get('chat_id')
        reply_markup_message_id = q.get('reply_markup_message_id')
        return UpdateChatReplyMarkup(chat_id, reply_markup_message_id)
