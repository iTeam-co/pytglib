

from ..utils import Object


class SetPollAnswer(Object):
    """
    Changes user answer to a poll 

    Attributes:
        ID (:obj:`str`): ``SetPollAnswer``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the poll belongs 
        message_id (:obj:`int`):
            Identifier of the message containing the poll
        option_ids (List of :obj:`int`):
            0-based identifiers of options, chosen by the userCurrently user can't choose more than 1 option

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
