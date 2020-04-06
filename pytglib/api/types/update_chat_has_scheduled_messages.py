

from ..utils import Object


class UpdateChatHasScheduledMessages(Object):
    """
    A chat's has_scheduled_messages field has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatHasScheduledMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        has_scheduled_messages (:obj:`bool`):
            New value of has_scheduled_messages

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatHasScheduledMessages"

    def __init__(self, chat_id, has_scheduled_messages, **kwargs):
        
        self.chat_id = chat_id  # int
        self.has_scheduled_messages = has_scheduled_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatHasScheduledMessages":
        chat_id = q.get('chat_id')
        has_scheduled_messages = q.get('has_scheduled_messages')
        return UpdateChatHasScheduledMessages(chat_id, has_scheduled_messages)
