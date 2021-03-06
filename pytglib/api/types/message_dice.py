

from ..utils import Object


class MessageDice(Object):
    """
    A dice message. The dice value is randomly generated by the server 

    Attributes:
        ID (:obj:`str`): ``MessageDice``

    Args:
        value (:obj:`int`):
            The dice value; 0-6If the value is 0, the dice must roll infinitely

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageDice"

    def __init__(self, value, **kwargs):
        
        self.value = value  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageDice":
        value = q.get('value')
        return MessageDice(value)
