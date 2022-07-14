

from ..utils import Object


class ChatStatisticsMessageSenderInfo(Object):
    """
    Contains statistics about messages sent by a user

    Attributes:
        ID (:obj:`str`): ``ChatStatisticsMessageSenderInfo``

    Args:
        user_id (:obj:`int`):
            User identifier
        sent_message_count (:obj:`int`):
            Number of sent messages
        average_character_count (:obj:`int`):
            Average number of characters in sent messages; 0 if unknown

    Returns:
        ChatStatisticsMessageSenderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatStatisticsMessageSenderInfo"

    def __init__(self, user_id, sent_message_count, average_character_count, **kwargs):
        
        self.user_id = user_id  # int
        self.sent_message_count = sent_message_count  # int
        self.average_character_count = average_character_count  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsMessageSenderInfo":
        user_id = q.get('user_id')
        sent_message_count = q.get('sent_message_count')
        average_character_count = q.get('average_character_count')
        return ChatStatisticsMessageSenderInfo(user_id, sent_message_count, average_character_count)
