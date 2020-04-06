

from ..utils import Object


class GetPollVoters(Object):
    """
    Returns users voted for the specified option in a non-anonymous polls. For the optimal performance the number of returned users is chosen by the library

    Attributes:
        ID (:obj:`str`): ``GetPollVoters``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat to which the poll belongs 
        message_id (:obj:`int`):
            Identifier of the message containing the poll
        option_id (:obj:`int`):
            0-based identifier of the answer option
        offset (:obj:`int`):
            Number of users to skip in the result; must be non-negative
        limit (:obj:`int`):
            The maximum number of users to be returned; must be positive and can't be greater than 50Fewer users may be returned than specified by the limit, even if the end of the voter list has not been reached

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPollVoters"

    def __init__(self, chat_id, message_id, option_id, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.option_id = option_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetPollVoters":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        option_id = q.get('option_id')
        offset = q.get('offset')
        limit = q.get('limit')
        return GetPollVoters(chat_id, message_id, option_id, offset, limit)
