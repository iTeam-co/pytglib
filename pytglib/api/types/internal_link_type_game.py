

from ..utils import Object


class InternalLinkTypeGame(Object):
    """
    The link is a link to a game. Call searchPublicChat with the given bot username, check that the user is a bot, ask the current user to select a chat to send the game, and then call sendMessage with inputMessageGame

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeGame``

    Args:
        bot_username (:obj:`str`):
            Username of the bot that owns the game 
        game_short_name (:obj:`str`):
            Short name of the game

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeGame"

    def __init__(self, bot_username, game_short_name, **kwargs):
        
        self.bot_username = bot_username  # str
        self.game_short_name = game_short_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeGame":
        bot_username = q.get('bot_username')
        game_short_name = q.get('game_short_name')
        return InternalLinkTypeGame(bot_username, game_short_name)
