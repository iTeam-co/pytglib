

from ..utils import Object


class SecretChatStateClosed(Object):
    """
    The secret chat is closed

    Attributes:
        ID (:obj:`str`): ``SecretChatStateClosed``

    No parameters required.

    Returns:
        SecretChatState

    Raises:
        :class:`telegram.Error`
    """
    ID = "secretChatStateClosed"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SecretChatStateClosed":
        
        return SecretChatStateClosed()
