

from ..utils import Object


class InternalLinkTypeAttachmentMenuBot(Object):
    """
    The link is a link to an attachment menu bot to be opened in the specified or a chosen chat. Process given target_chat to open the chat.Then call searchPublicChat with the given bot username, check that the user is a bot and can be added to attachment menu. Then use getAttachmentMenuBot to receive information about the bot.If the bot isn't added to attachment menu, then user needs to confirm adding the bot to attachment menu. If user confirms adding, then use toggleBotIsAddedToAttachmentMenu to add it.If the attachment menu bot can't be used in the opened chat, show an error to the user. If the bot is added to attachment menu and can be used in the chat, then use openWebApp with the given URL

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeAttachmentMenuBot``

    Args:
        target_chat (:class:`telegram.api.types.TargetChat`):
            Target chat to be opened 
        bot_username (:obj:`str`):
            Username of the bot 
        url (:obj:`str`):
            URL to be passed to openWebApp

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeAttachmentMenuBot"

    def __init__(self, target_chat, bot_username, url, **kwargs):
        
        self.target_chat = target_chat  # TargetChat
        self.bot_username = bot_username  # str
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeAttachmentMenuBot":
        target_chat = Object.read(q.get('target_chat'))
        bot_username = q.get('bot_username')
        url = q.get('url')
        return InternalLinkTypeAttachmentMenuBot(target_chat, bot_username, url)
