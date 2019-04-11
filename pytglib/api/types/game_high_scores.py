

from ..utils import Object


class GameHighScores(Object):
    """
    Contains a list of game high scores 

    Attributes:
        ID (:obj:`str`): ``GameHighScores``

    Args:
        scores (List of :class:`telegram.api.types.gameHighScore`):
            A list of game high scores

    Returns:
        GameHighScores

    Raises:
        :class:`telegram.Error`
    """
    ID = "gameHighScores"

    def __init__(self, scores, **kwargs):
        
        self.scores = scores  # list of gameHighScore

    @staticmethod
    def read(q: dict, *args) -> "GameHighScores":
        scores = [Object.read(i) for i in q.get('scores', [])]
        return GameHighScores(scores)
