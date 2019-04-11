

from ..utils import Object


class InputMessageGame(Object):
    """
    A message with a game; not supported for channels or secret chats 

    Attributes:
        ID (:obj:`str`): ``InputMessageGame``

    Args:
        bot_user_id (:obj:`int`):
            User identifier of the bot that owns the game 
        game_short_name (:obj:`str`):
            Short name of the game

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageGame"

    def __init__(self, bot_user_id, game_short_name, **kwargs):
        
        self.bot_user_id = bot_user_id  # int
        self.game_short_name = game_short_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InputMessageGame":
        bot_user_id = q.get('bot_user_id')
        game_short_name = q.get('game_short_name')
        return InputMessageGame(bot_user_id, game_short_name)
