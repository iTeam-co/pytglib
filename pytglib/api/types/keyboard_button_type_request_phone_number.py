

from ..utils import Object


class KeyboardButtonTypeRequestPhoneNumber(Object):
    """
    A button that sends the user's phone number when pressed; available only in private chats

    Attributes:
        ID (:obj:`str`): ``KeyboardButtonTypeRequestPhoneNumber``

    No parameters required.

    Returns:
        KeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButtonTypeRequestPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeRequestPhoneNumber":
        
        return KeyboardButtonTypeRequestPhoneNumber()
