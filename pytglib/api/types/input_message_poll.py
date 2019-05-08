

from ..utils import Object


class InputMessagePoll(Object):
    """
    A message with a poll. Polls can't be sent to private or secret chats 

    Attributes:
        ID (:obj:`str`): ``InputMessagePoll``

    Args:
        question (:obj:`str`):
            Poll question, 1-255 characters 
        options (List of :obj:`str`):
            List of poll answer options, 2-10 strings 1-100 characters each

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessagePoll"

    def __init__(self, question, options, **kwargs):
        
        self.question = question  # str
        self.options = options  # list of str

    @staticmethod
    def read(q: dict, *args) -> "InputMessagePoll":
        question = q.get('question')
        options = q.get('options')
        return InputMessagePoll(question, options)
