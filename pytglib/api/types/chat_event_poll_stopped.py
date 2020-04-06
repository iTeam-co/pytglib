

from ..utils import Object


class ChatEventPollStopped(Object):
    """
    A poll in a message was stopped 

    Attributes:
        ID (:obj:`str`): ``ChatEventPollStopped``

    Args:
        message (:class:`telegram.api.types.message`):
            The message with the poll

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventPollStopped"

    def __init__(self, message, **kwargs):
        
        self.message = message  # Message

    @staticmethod
    def read(q: dict, *args) -> "ChatEventPollStopped":
        message = Object.read(q.get('message'))
        return ChatEventPollStopped(message)
