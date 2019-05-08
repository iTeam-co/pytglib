

from ..utils import Object


class PushMessageContentMessageForwards(Object):
    """
    A forwarded messages 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentMessageForwards``

    Args:
        total_count (:obj:`int`):
            Number of forwarded messages

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentMessageForwards"

    def __init__(self, total_count, **kwargs):
        
        self.total_count = total_count  # int

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentMessageForwards":
        total_count = q.get('total_count')
        return PushMessageContentMessageForwards(total_count)
