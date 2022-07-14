

from ..utils import Object


class TextEntityTypeBotCommand(Object):
    """
    A bot command, beginning with "/"

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeBotCommand``

    No parameters required.

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeBotCommand"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeBotCommand":
        
        return TextEntityTypeBotCommand()
