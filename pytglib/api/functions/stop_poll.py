

from ..utils import Object


class StopPoll(Object):
    """
    Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set

    Attributes:
        ID (:obj:`str`): ``StopPoll``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the poll belongs 
        message_id (:obj:`int`):
            Identifier of the message containing the poll 
        reply_markup (:class:`telegram.api.types.ReplyMarkup`):
            The new message reply markup; for bots only

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "stopPoll"

    def __init__(self, chat_id, message_id, reply_markup, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(q: dict, *args) -> "StopPoll":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        reply_markup = Object.read(q.get('reply_markup'))
        return StopPoll(chat_id, message_id, reply_markup)
