

from ..utils import Object


class SetPollAnswer(Object):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once

    Attributes:
        ID (:obj:`str`): ``SetPollAnswer``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the poll belongs 
        message_id (:obj:`int`):
            Identifier of the message containing the poll
        option_ids (List of :obj:`int`):
            0-based identifiers of answer options, chosen by the userUser can choose more than 1 answer option only is the poll allows multiple answers

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPollAnswer"

    def __init__(self, chat_id, message_id, option_ids, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.option_ids = option_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "SetPollAnswer":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        option_ids = q.get('option_ids')
        return SetPollAnswer(chat_id, message_id, option_ids)
