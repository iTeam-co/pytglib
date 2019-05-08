

from ..utils import Object


class SetGameScore(Object):
    """
    Updates the game score of the specified user in the game; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetGameScore``

    Args:
        chat_id (:obj:`int`):
            The chat to which the message with the game belongs 
        message_id (:obj:`int`):
            Identifier of the message 
        edit_message (:obj:`bool`):
            True, if the message should be edited 
        user_id (:obj:`int`):
            User identifier 
        score (:obj:`int`):
            The new score
        force (:obj:`bool`):
            Pass true to update the score even if it decreasesIf the score is 0, the user will be deleted from the high score table

    Returns:
        Message

    Raises:
        :class:`telegram.Error`
    """
    ID = "setGameScore"

    def __init__(self, chat_id, message_id, edit_message, user_id, score, force, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.edit_message = edit_message  # bool
        self.user_id = user_id  # int
        self.score = score  # int
        self.force = force  # bool

    @staticmethod
    def read(q: dict, *args) -> "SetGameScore":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        edit_message = q.get('edit_message')
        user_id = q.get('user_id')
        score = q.get('score')
        force = q.get('force')
        return SetGameScore(chat_id, message_id, edit_message, user_id, score, force)
