

from ..utils import Object


class SetInlineGameScore(Object):
    """
    Updates the game score of the specified user in a game; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetInlineGameScore``

    Args:
        inline_message_id (:obj:`str`):
            Inline message identifier 
        edit_message (:obj:`bool`):
            True, if the message should be edited 
        user_id (:obj:`int`):
            User identifier 
        score (:obj:`int`):
            The new score
        force (:obj:`bool`):
            Pass true to update the score even if it decreasesIf the score is 0, the user will be deleted from the high score table

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setInlineGameScore"

    def __init__(self, inline_message_id, edit_message, user_id, score, force, extra=None, **kwargs):
        self.extra = extra
        self.inline_message_id = inline_message_id  # str
        self.edit_message = edit_message  # bool
        self.user_id = user_id  # int
        self.score = score  # int
        self.force = force  # bool

    @staticmethod
    def read(q: dict, *args) -> "SetInlineGameScore":
        inline_message_id = q.get('inline_message_id')
        edit_message = q.get('edit_message')
        user_id = q.get('user_id')
        score = q.get('score')
        force = q.get('force')
        return SetInlineGameScore(inline_message_id, edit_message, user_id, score, force)
