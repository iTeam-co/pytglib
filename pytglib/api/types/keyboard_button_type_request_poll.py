

from ..utils import Object


class KeyboardButtonTypeRequestPoll(Object):
    """
    A button that allows the user to create and send a poll when pressed; available only in private chats 

    Attributes:
        ID (:obj:`str`): ``KeyboardButtonTypeRequestPoll``

    Args:
        force_regular (:obj:`bool`):
            If true, only regular polls must be allowed to create 
        force_quiz (:obj:`bool`):
            If true, only polls in quiz mode must be allowed to create

    Returns:
        KeyboardButtonType

    Raises:
        :class:`telegram.Error`
    """
    ID = "keyboardButtonTypeRequestPoll"

    def __init__(self, force_regular, force_quiz, **kwargs):
        
        self.force_regular = force_regular  # bool
        self.force_quiz = force_quiz  # bool

    @staticmethod
    def read(q: dict, *args) -> "KeyboardButtonTypeRequestPoll":
        force_regular = q.get('force_regular')
        force_quiz = q.get('force_quiz')
        return KeyboardButtonTypeRequestPoll(force_regular, force_quiz)
