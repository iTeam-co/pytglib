

from ..utils import Object


class ReplyMarkupShowKeyboard(Object):
    """
    Contains a custom keyboard layout to quickly reply to bots

    Attributes:
        ID (:obj:`str`): ``ReplyMarkupShowKeyboard``

    Args:
        rows (List of List of :class:`telegram.api.types.keyboardButton`):
            A list of rows of bot keyboard buttons
        resize_keyboard (:obj:`bool`):
            True, if the client needs to resize the keyboard vertically
        one_time (:obj:`bool`):
            True, if the client needs to hide the keyboard after use
        is_personal (:obj:`bool`):
            True, if the keyboard must automatically be shown to the current userFor outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply

    Returns:
        ReplyMarkup

    Raises:
        :class:`telegram.Error`
    """
    ID = "replyMarkupShowKeyboard"

    def __init__(self, rows, resize_keyboard, one_time, is_personal, **kwargs):
        
        self.rows = rows  # list of list(keyboardButton)
        self.resize_keyboard = resize_keyboard  # bool
        self.one_time = one_time  # bool
        self.is_personal = is_personal  # bool

    @staticmethod
    def read(q: dict, *args) -> "ReplyMarkupShowKeyboard":
        rows = [[Object.read(v) for v in i] for i in q.get('rows', [])]
        resize_keyboard = q.get('resize_keyboard')
        one_time = q.get('one_time')
        is_personal = q.get('is_personal')
        return ReplyMarkupShowKeyboard(rows, resize_keyboard, one_time, is_personal)
