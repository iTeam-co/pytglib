

from ..utils import Object


class GetAttachmentMenuBot(Object):
    """
    Returns information about a bot that can be added to attachment menu 

    Attributes:
        ID (:obj:`str`): ``GetAttachmentMenuBot``

    Args:
        bot_user_id (:obj:`int`):
            Bot's user identifier

    Returns:
        AttachmentMenuBot

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAttachmentMenuBot"

    def __init__(self, bot_user_id, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetAttachmentMenuBot":
        bot_user_id = q.get('bot_user_id')
        return GetAttachmentMenuBot(bot_user_id)
