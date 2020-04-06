

from ..utils import Object


class ChatStatisticsMessageInteractionCounters(Object):
    """
    Contains statistics about interactions with a message

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsMessageInteractionCounters``

    Args:
        message_id (:obj:`int`):
            Message identifier
        view_count (:obj:`int`):
            Number of times the message was viewed
        forward_count (:obj:`int`):
            Number of times the message was forwarded

    Returns:
        ChatStatisticsMessageInteractionCounters

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsMessageInteractionCounters"

    def __init__(self, message_id, view_count, forward_count, **kwargs):
        
        self.message_id = message_id  # int
        self.view_count = view_count  # int
        self.forward_count = forward_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsMessageInteractionCounters":
        message_id = q.get('message_id')
        view_count = q.get('view_count')
        forward_count = q.get('forward_count')
        return ChatStatisticsMessageInteractionCounters(message_id, view_count, forward_count)
