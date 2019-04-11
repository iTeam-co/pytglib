

from ..utils import Object


class SecretChatStatePending(Object):
    """
    The secret chat is not yet created; waiting for the other user to get online

    Attributes:
        ID (:obj:`str`): ``SecretChatStatePending``

    No parameters required.

    Returns:
        SecretChatState

    Raises:
        :class:`telegram.Error`
    """
    ID = "secretChatStatePending"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SecretChatStatePending":
        
        return SecretChatStatePending()
