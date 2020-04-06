

from ..utils import Object


class MessageGame(Object):
    """
    A message with a game 

    Attributes:
        ID (:obj:`str`): ``MessageGame``

    Args:
        game (:class:`telegram.api.types.game`):
            The game description

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageGame"

    def __init__(self, game, **kwargs):
        
        self.game = game  # Game

    @staticmethod
    def read(q: dict, *args) -> "MessageGame":
        game = Object.read(q.get('game'))
        return MessageGame(game)
