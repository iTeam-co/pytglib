

from ..utils import Object


class SecretChatState(Object):
    """
    Describes the current secret chat state

    No parameters required.
    """
    ID = "secretChatState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SecretChatStateReady or SecretChatStateClosed or SecretChatStatePending":
        if q.get("@type"):
            return Object.read(q)
        return SecretChatState()
