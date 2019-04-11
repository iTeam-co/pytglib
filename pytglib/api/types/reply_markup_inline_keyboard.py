

from ..utils import Object


class ReplyMarkupInlineKeyboard(Object):
    """
    Contains an inline keyboard layout

    Attributes:
        ID (:obj:`str`): ``ReplyMarkupInlineKeyboard``

    Args:
        rows (List of List of :class:`telegram.api.types.inlineKeyboardButton`):
            A list of rows of inline keyboard buttons

    Returns:
        ReplyMarkup

    Raises:
        :class:`telegram.Error`
    """
    ID = "replyMarkupInlineKeyboard"

    def __init__(self, rows, **kwargs):
        
        self.rows = rows  # list of list(inlineKeyboardButton)

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupInlineKeyboard":
        rows = [[Object.read(v) for v in i] for i in q.get('rows', [])]
        return ReplyMarkupInlineKeyboard(rows)
