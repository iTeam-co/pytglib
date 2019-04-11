

from ..utils import Object


class CallbackQueryPayloadGame(Object):
    """
    The payload from a game callback button 

    Attributes:
        ID (:obj:`str`): ``CallbackQueryPayloadGame``

    Args:
        game_short_name (:obj:`str`):
            A short name of the game that was attached to the callback button

    Returns:
        CallbackQueryPayload

    Raises:
        :class:`telegram.Error`
    """
    ID = "callbackQueryPayloadGame"

    def __init__(self, game_short_name, **kwargs):
        
        self.game_short_name = game_short_name  # str

    @staticmethod
    def read(q: dict, *args) -> "CallbackQueryPayloadGame":
        game_short_name = q.get('game_short_name')
        return CallbackQueryPayloadGame(game_short_name)
