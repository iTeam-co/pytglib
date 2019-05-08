

from ..utils import Object


class CheckChatUsernameResult(Object):
    """
    Represents result of checking whether a username can be set for a chat

    No parameters required.
    """
    ID = "checkChatUsernameResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultUsernameInvalid or CheckChatUsernameResultUsernameOccupied or CheckChatUsernameResultOk or CheckChatUsernameResultPublicGroupsUnavailable or CheckChatUsernameResultPublicChatsTooMuch":
        if q.get("@type"):
            return Object.read(q)
        return CheckChatUsernameResult()
