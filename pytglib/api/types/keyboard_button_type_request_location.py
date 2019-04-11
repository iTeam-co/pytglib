

from ..utils import Object


class KeyboardButtonTypeRequestLocation(Object):
    """
    A button that sends the user's location when pressed; available only in private chats

    Attributes:
        ID (:obj:`str`): ``KeyboardButtonTypeRequestLocation``

    No parameters required.

    Returns:
        KeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButtonTypeRequestLocation"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeRequestLocation":
        
        return KeyboardButtonTypeRequestLocation()
