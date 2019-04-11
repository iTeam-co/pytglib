

from ..utils import Object


class ChatActionStartPlayingGame(Object):
    """
    The user has started to play a game

    Attributes:
        ID (:obj:`str`): ``ChatActionStartPlayingGame``

    No parameters required.

    Returns:
        ChatAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatActionStartPlayingGame"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatActionStartPlayingGame":
        
        return ChatActionStartPlayingGame()
