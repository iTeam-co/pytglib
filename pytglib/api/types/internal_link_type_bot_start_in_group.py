

from ..utils import Object


class InternalLinkTypeBotStartInGroup(Object):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a group chat. Call searchPublicChat with the given bot username, check that the user is a bot and can be added to groups,ask the current user to select a basic group or a supergroup chat to add the bot to, taking into account that bots can be added to a public supergroup only by administrators of the supergroup.If administrator rights are provided by the link, call getChatMember to receive the current bot rights in the chat and if the bot already is an administrator,check that the current user can edit its administrator rights, combine received rights with the requested administrator rights, show confirmation box to the user,and call setChatMemberStatus with the chosen chat and confirmed administrator rights. Before call to setChatMemberStatus it may be required to upgrade the chosen basic group chat to a supergroup chat.Then if start_parameter isn't empty, call sendBotStartMessage with the given start parameter and the chosen chat, otherwise just send /start message with bot's username added to the chat.

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeBotStartInGroup``

    Args:
        bot_username (:obj:`str`):
            Username of the bot 
        start_parameter (:obj:`str`):
            The parameter to be passed to sendBotStartMessage 
        administrator_rights (:class:`telegram.api.types.chatAdministratorRights`):
            Expected administrator rights for the bot; may be null

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeBotStartInGroup"

    def __init__(self, bot_username, start_parameter, administrator_rights, **kwargs):
        
        self.bot_username = bot_username  # str
        self.start_parameter = start_parameter  # str
        self.administrator_rights = administrator_rights  # ChatAdministratorRights

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeBotStartInGroup":
        bot_username = q.get('bot_username')
        start_parameter = q.get('start_parameter')
        administrator_rights = Object.read(q.get('administrator_rights'))
        return InternalLinkTypeBotStartInGroup(bot_username, start_parameter, administrator_rights)
