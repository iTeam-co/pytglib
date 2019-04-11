

from ..utils import Object


class GetInlineGameHighScores(Object):
    """
    Returns game high scores and some part of the high score table in the range of the specified user; for bots only 

    Attributes:
        ID (:obj:`str`): ``GetInlineGameHighScores``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        user_id (:obj:`int`):
            User identifier

    Returns:
        GameHighScores

    Raises:
        :class:`telegram.Error`
    """
    ID = "getInlineGameHighScores"

    def __init__(self, inline_message_id, user_id, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetInlineGameHighScores":
        inline_message_id = q.get('inline_message_id')
        user_id = q.get('user_id')
        return GetInlineGameHighScores(inline_message_id, user_id)
