

from ..utils import Object


class CheckChatUsernameResultPublicChatsTooMuch(Object):
    """
    The user has too many chats with username, one of them must be made private first

    Attributes:
        ID (:obj:`str`): ``CheckChatUsernameResultPublicChatsTooMuch``

    No parameters required.

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsernameResultPublicChatsTooMuch"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultPublicChatsTooMuch":
        
        return CheckChatUsernameResultPublicChatsTooMuch()
