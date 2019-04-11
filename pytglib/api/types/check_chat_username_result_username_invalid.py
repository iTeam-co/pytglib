

from ..utils import Object


class CheckChatUsernameResultUsernameInvalid(Object):
    """
    The username is invalid

    Attributes:
        ID (:obj:`str`): ``CheckChatUsernameResultUsernameInvalid``

    No parameters required.

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsernameResultUsernameInvalid"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultUsernameInvalid":
        
        return CheckChatUsernameResultUsernameInvalid()
