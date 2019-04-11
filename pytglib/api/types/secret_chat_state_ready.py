

from ..utils import Object


class SecretChatStateReady(Object):
    """
    The secret chat is ready to use

    Attributes:
        ID (:obj:`str`): ``SecretChatStateReady``

    No parameters required.

    Returns:
        SecretChatState

    Raises:
        :class:`telegram.Error`
    """
    ID = "secretChatStateReady"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SecretChatStateReady":
        
        return SecretChatStateReady()
