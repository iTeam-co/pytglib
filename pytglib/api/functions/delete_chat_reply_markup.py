

from ..utils import Object


class DeleteChatReplyMarkup(Object):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup will be changed 

    Attributes:
        ID (:obj:`str`): ``DeleteChatReplyMarkup``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        message_id (:obj:`int`):
            The message identifier of the used keyboard

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatReplyMarkup"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatReplyMarkup":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return DeleteChatReplyMarkup(chat_id, message_id)
