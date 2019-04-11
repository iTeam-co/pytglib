

from ..utils import Object


class InlineKeyboardButtonType(Object):
    """
    Describes the type of an inline keyboard button

    No parameters required.
    """
    ID = "inlineKeyboardButtonType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeBuy or InlineKeyboardButtonTypeSwitchInline or InlineKeyboardButtonTypeCallback or InlineKeyboardButtonTypeUrl or InlineKeyboardButtonTypeCallbackGame":
        if q.get("@type"):
            return Object.read(q)
        return InlineKeyboardButtonType()
