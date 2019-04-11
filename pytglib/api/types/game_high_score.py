

from ..utils import Object


class GameHighScore(Object):
    """
    Contains one row of the game high score table 

    Attributes:
        ID (:obj:`str`): ``GameHighScore``

    Args:
        position (:obj:`int`):
            Position in the high score table 
        user_id (:obj:`int`):
            User identifier 
        score (:obj:`int`):
            User score

    Returns:
        GameHighScore

    Raises:
        :class:`telegram.Error`
    """
    ID = "gameHighScore"

    def __init__(self, position, user_id, score, **kwargs):
        
        self.position = position  # int
        self.user_id = user_id  # int
        self.score = score  # int

    @staticmethod
    def read(q: dict, *args) -> "GameHighScore":
        position = q.get('position')
        user_id = q.get('user_id')
        score = q.get('score')
        return GameHighScore(position, user_id, score)
