

from ..utils import Object


class InputMessageDice(Object):
    """
    A dice message

    Attributes:
        ID (:obj:`str`): ``InputMessageDice``

    No parameters required.

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageDice"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputMessageDice":
        
        return InputMessageDice()
