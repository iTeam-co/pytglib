

from ..utils import Object


class CheckChatUsernameResultUsernameOccupied(Object):
    """
    The username is occupied

    Attributes:
        ID (:obj:`str`): ``CheckChatUsernameResultUsernameOccupied``

    No parameters required.

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsernameResultUsernameOccupied"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultUsernameOccupied":
        
        return CheckChatUsernameResultUsernameOccupied()
