

from ..utils import Object


class MessagePoll(Object):
    """
    A message with a poll 

    Attributes:
        ID (:obj:`str`): ``MessagePoll``

    Args:
        poll (:class:`telegram.api.types.poll`):
            The poll description

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePoll"

    def __init__(self, poll, **kwargs):
        
        self.poll = poll  # Poll

    @staticmethod
    def read(q: dict, *args) -> "MessagePoll":
        poll = Object.read(q.get('poll'))
        return MessagePoll(poll)
