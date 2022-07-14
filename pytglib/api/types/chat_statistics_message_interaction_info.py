

from ..utils import Object


class ChatStatisticsMessageInteractionInfo(Object):
    """
    Contains statistics about interactions with a message

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsMessageInteractionInfo``

    Args:
        message_id (:obj:`int`):
            Message identifier
        view_count (:obj:`int`):
            Number of times the message was viewed
        forward_count (:obj:`int`):
            Number of times the message was forwarded

    Returns:
        ChatStatisticsMessageInteractionInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsMessageInteractionInfo"

    def __init__(self, message_id, view_count, forward_count, **kwargs):
        
        self.message_id = message_id  # int
        self.view_count = view_count  # int
        self.forward_count = forward_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsMessageInteractionInfo":
        message_id = q.get('message_id')
        view_count = q.get('view_count')
        forward_count = q.get('forward_count')
        return ChatStatisticsMessageInteractionInfo(message_id, view_count, forward_count)
