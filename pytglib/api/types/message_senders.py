

from ..utils import Object


class MessageSenders(Object):
    """
    Represents a list of message senders 

    Attributes:
        ID (:obj:`str`): ``MessageSenders``

    Args:
        total_count (:obj:`int`):
            Approximate total number of messages senders found 
        senders (List of :class:`telegram.api.types.MessageSender`):
            List of message senders

    Returns:
        MessageSenders

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSenders"

    def __init__(self, total_count, senders, **kwargs):
        
        self.total_count = total_count  # int
        self.senders = senders  # list of MessageSender

    @staticmethod
    def read(q: dict, *args) -> "MessageSenders":
        total_count = q.get('total_count')
        senders = [Object.read(i) for i in q.get('senders', [])]
        return MessageSenders(total_count, senders)
