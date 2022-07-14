

from ..utils import Object


class KeyboardButtonType(Object):
    """
    Describes a keyboard button type

    No parameters required.
    """
    ID = "keyboardButtonType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeRequestLocation or KeyboardButtonTypeRequestPhoneNumber or KeyboardButtonTypeRequestPoll or KeyboardButtonTypeWebApp or KeyboardButtonTypeText":
        if q.get("@type"):
            return Object.read(q)
        return KeyboardButtonType()
