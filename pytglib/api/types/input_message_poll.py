

from ..utils import Object


class InputMessagePoll(Object):
    """
    A message with a poll. Polls can't be sent to secret chats. Polls can be sent only to a private chat with a bot 

    Attributes:
        ID (:obj:`str`): ``InputMessagePoll``

    Args:
        question (:obj:`str`):
            Poll question; 1-255 characters (up to 300 characters for bots) 
        options (List of :obj:`str`):
            List of poll answer options, 2-10 strings 1-100 characters each
        is_anonymous (:obj:`bool`):
            True, if the poll voters are anonymousNon-anonymous polls can't be sent or forwarded to channels 
        type (:class:`telegram.api.types.PollType`):
            Type of the poll
        open_period (:obj:`int`):
            Amount of time the poll will be active after creation, in seconds; for bots only
        close_date (:obj:`int`):
            Point in time (Unix timestamp) when the poll will automatically be closed; for bots only
        is_closed (:obj:`bool`):
            True, if the poll needs to be sent already closed; for bots only

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessagePoll"

    def __init__(self, question, options, is_anonymous, type, open_period, close_date, is_closed, **kwargs):
        
        self.question = question  # str
        self.options = options  # list of str
        self.is_anonymous = is_anonymous  # bool
        self.type = type  # PollType
        self.open_period = open_period  # int
        self.close_date = close_date  # int
        self.is_closed = is_closed  # bool

    @staticmethod
    def read(q: dict, *args) -> "InputMessagePoll":
        question = q.get('question')
        options = q.get('options')
        is_anonymous = q.get('is_anonymous')
        type = Object.read(q.get('type'))
        open_period = q.get('open_period')
        close_date = q.get('close_date')
        is_closed = q.get('is_closed')
        return InputMessagePoll(question, options, is_anonymous, type, open_period, close_date, is_closed)
