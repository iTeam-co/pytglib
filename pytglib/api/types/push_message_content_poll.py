

from ..utils import Object


class PushMessageContentPoll(Object):
    """
    A message with a poll 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentPoll``

    Args:
        question (:obj:`str`):
            Poll question 
        is_regular (:obj:`bool`):
            True, if the poll is regular and not in quiz mode 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentPoll"

    def __init__(self, question, is_regular, is_pinned, **kwargs):
        
        self.question = question  # str
        self.is_regular = is_regular  # bool
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentPoll":
        question = q.get('question')
        is_regular = q.get('is_regular')
        is_pinned = q.get('is_pinned')
        return PushMessageContentPoll(question, is_regular, is_pinned)
