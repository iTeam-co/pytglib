

from ..utils import Object


class MessageCustomServiceAction(Object):
    """
    A non-standard action has happened in the chat 

    Attributes:
        ID (:obj:`str`): ``MessageCustomServiceAction``

    Args:
        text (:obj:`str`):
            Message text to be shown in the chat

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageCustomServiceAction"

    def __init__(self, text, **kwargs):
        
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageCustomServiceAction":
        text = q.get('text')
        return MessageCustomServiceAction(text)
