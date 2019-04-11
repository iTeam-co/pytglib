

from ..utils import Object


class InlineQueryResultGame(Object):
    """
    Represents information about a game 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultGame``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        game (:class:`telegram.api.types.game`):
            Game result

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultGame"

    def __init__(self, id, game, **kwargs):
        
        self.id = id  # str
        self.game = game  # Game

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultGame":
        id = q.get('id')
        game = Object.read(q.get('game'))
        return InlineQueryResultGame(id, game)
