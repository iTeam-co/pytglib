

from ..utils import Object


class KeyboardButtonTypeText(Object):
    """
    A simple button, with text that should be sent when the button is pressed

    Attributes:
        ID (:obj:`str`): ``KeyboardButtonTypeText``

    No parameters required.

    Returns:
        KeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButtonTypeText"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeText":
        
        return KeyboardButtonTypeText()
