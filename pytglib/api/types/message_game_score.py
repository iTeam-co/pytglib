

from ..utils import Object


class MessageGameScore(Object):
    """
    A new high score was achieved in a game 

    Attributes:
        ID (:obj:`str`): ``MessageGameScore``

    Args:
        game_message_id (:obj:`int`):
            Identifier of the message with the game, can be an identifier of a deleted message 
        game_id (:obj:`int`):
            Identifier of the game; may be different from the games presented in the message with the game 
        score (:obj:`int`):
            New score

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageGameScore"

    def __init__(self, game_message_id, game_id, score, **kwargs):
        
        self.game_message_id = game_message_id  # int
        self.game_id = game_id  # int
        self.score = score  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageGameScore":
        game_message_id = q.get('game_message_id')
        game_id = q.get('game_id')
        score = q.get('score')
        return MessageGameScore(game_message_id, game_id, score)
