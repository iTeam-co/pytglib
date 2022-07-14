

from ..utils import Object


class InlineKeyboardButtonTypeUser(Object):
    """
    A button with a user reference to be handled in the same way as textEntityTypeMentionName entities 

    Attributes:
        ID (:obj:`str`): ``InlineKeyboardButtonTypeUser``

    Args:
        user_id (:obj:`int`):
            User identifier

    Returns:
        InlineKeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineKeyboardButtonTypeUser"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "InlineKeyboardButtonTypeUser":
        user_id = q.get('user_id')
        return InlineKeyboardButtonTypeUser(user_id)
