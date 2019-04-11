

from ..utils import Object


class InlineKeyboardButtonTypeBuy(Object):
    """
    A button to buy something. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageInvoice

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeBuy``

    No parameters required.

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeBuy"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeBuy":
        
        return InlineKeyboardButtonTypeBuy()
