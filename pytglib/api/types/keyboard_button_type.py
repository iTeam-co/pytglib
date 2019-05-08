

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
    def read(q: dict, *args) -> "KeyboardButtonTypeRequestPhoneNumber or KeyboardButtonTypeText or KeyboardButtonTypeRequestLocation":
        if q.get("@type"):
            return Object.read(q)
        return KeyboardButtonType()
