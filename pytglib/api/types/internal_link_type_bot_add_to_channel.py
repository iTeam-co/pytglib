

from ..utils import Object


class InternalLinkTypeBotAddToChannel(Object):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a channel chat as an administrator. Call searchPublicChat with the given bot username and check that the user is a bot,ask the current user to select a channel chat to add the bot to as an administrator. Then call getChatMember to receive the current bot rights in the chat and if the bot already is an administrator,check that the current user can edit its administrator rights and combine received rights with the requested administrator rights. Then show confirmation box to the user, and call setChatMemberStatus with the chosen chat and confirmed rights

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeBotAddToChannel``

    Args:
        bot_username (:obj:`str`):
            Username of the bot 
        administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Expected administrator rights for the bot

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeBotAddToChannel"

    def __init__(self, bot_username, administrator_rights, **kwargs):
        
        self.bot_username = bot_username  # str
        self.administrator_rights = administrator_rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeBotAddToChannel":
        bot_username = q.get('bot_username')
        administrator_rights = Object.read(q.get('administrator_rights'))
        return InternalLinkTypeBotAddToChannel(bot_username, administrator_rights)
