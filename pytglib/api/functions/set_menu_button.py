

from ..utils import Object


class SetMenuButton(Object):
    """
    Sets menu button for the given user or for all users; for bots only

    Attributes:
        ID (:obj:`str`): ``SetMenuButton``

    Args:
        user_id (:obj:`int`):
            Identifier of the user or 0 to set menu button for all users
        menu_button (:class:`telegram.api.types.botMenuButton`):
            New menu button

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setMenuButton"

    def __init__(self, user_id, menu_button, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.menu_button = menu_button  # BotMenuButton

    @staticmethod
    def read(q: dict, *args) -> "SetMenuButton":
        user_id = q.get('user_id')
        menu_button = Object.read(q.get('menu_button'))
        return SetMenuButton(user_id, menu_button)
