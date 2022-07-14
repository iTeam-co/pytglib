

from ..utils import Object


class GetMenuButton(Object):
    """
    Returns menu button set by the bot for the given user; for bots only 

    Attributes:
        ID (:obj:`str`): ``GetMenuButton``

    Args:
        user_id (:obj:`int`):
            Identifier of the user or 0 to get the default menu button

    Returns:
        BotMenuButton

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMenuButton"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMenuButton":
        user_id = q.get('user_id')
        return GetMenuButton(user_id)
