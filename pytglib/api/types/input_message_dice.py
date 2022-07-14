

from ..utils import Object


class InputMessageDice(Object):
    """
    A dice message 

    Attributes:
        ID (:obj:`str`): ``InputMessageDice``

    Args:
        emoji (:obj:`str`):
            Emoji on which the dice throw animation is based 
        clear_draft (:obj:`bool`):
            True, if the chat message draft must be deleted

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageDice"

    def __init__(self, emoji, clear_draft, **kwargs):
        
        self.emoji = emoji  # str
        self.clear_draft = clear_draft  # bool

    @staticmethod
    def read(q: dict, *args) -> "InputMessageDice":
        emoji = q.get('emoji')
        clear_draft = q.get('clear_draft')
        return InputMessageDice(emoji, clear_draft)
