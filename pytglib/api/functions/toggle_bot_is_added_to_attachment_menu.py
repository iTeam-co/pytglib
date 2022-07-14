

from ..utils import Object


class ToggleBotIsAddedToAttachmentMenu(Object):
    """
    Adds or removes a bot to attachment menu. Bot can be added to attachment menu, only if userTypeBot.can_be_added_to_attachment_menu == true 

    Attributes:
        ID (:obj:`str`): ``ToggleBotIsAddedToAttachmentMenu``

    Args:
        bot_user_id (:obj:`int`):
            Bot's user identifier 
        is_added (:obj:`bool`):
            Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleBotIsAddedToAttachmentMenu"

    def __init__(self, bot_user_id, is_added, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.is_added = is_added  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleBotIsAddedToAttachmentMenu":
        bot_user_id = q.get('bot_user_id')
        is_added = q.get('is_added')
        return ToggleBotIsAddedToAttachmentMenu(bot_user_id, is_added)
