

from ..utils import Object


class GetGameHighScores(Object):
    """
    Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only 

    Attributes:
        ID (:obj:`str`): ``GetGameHighScores``

    Args:
        chat_id (:obj:`int`):
            The chat that contains the message with the game 
        message_id (:obj:`int`):
            Identifier of the message 
        user_id (:obj:`int`):
            User identifier

    Returns:
        GameHighScores

    Raises:
        :class:`telegram.Error`
    """
    ID = "getGameHighScores"

    def __init__(self, chat_id, message_id, user_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetGameHighScores":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        user_id = q.get('user_id')
        return GetGameHighScores(chat_id, message_id, user_id)
