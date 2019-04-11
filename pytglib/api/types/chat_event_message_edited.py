

from ..utils import Object


class ChatEventMessageEdited(Object):
    """
    A message was edited 

    Attributes:
        ID (:obj:`str`): ``ChatEventMessageEdited``

    Args:
        old_message (:class:`telegram.api.types.message`):
            The original message before the edit 
        new_message (:class:`telegram.api.types.message`):
            The message after it was edited

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessageEdited"

    def __init__(self, old_message, new_message, **kwargs):
        
        self.old_message = old_message  # Message
        self.new_message = new_message  # Message

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessageEdited":
        old_message = Object.read(q.get('old_message'))
        new_message = Object.read(q.get('new_message'))
        return ChatEventMessageEdited(old_message, new_message)
