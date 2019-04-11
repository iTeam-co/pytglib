

from ..utils import Object


class CheckChatUsernameResultOk(Object):
    """
    The username can be set

    Attributes:
        ID (:obj:`str`): ``CheckChatUsernameResultOk``

    No parameters required.

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsernameResultOk"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultOk":
        
        return CheckChatUsernameResultOk()
