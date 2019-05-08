

from ..utils import Object


class PushMessageContentPoll(Object):
    """
    A message with a poll 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentPoll``

    Args:
        question (:obj:`str`):
            Poll question 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentPoll"

    def __init__(self, question, is_pinned, **kwargs):
        
        self.question = question  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentPoll":
        question = q.get('question')
        is_pinned = q.get('is_pinned')
        return PushMessageContentPoll(question, is_pinned)
