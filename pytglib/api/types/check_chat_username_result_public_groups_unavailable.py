

from ..utils import Object


class CheckChatUsernameResultPublicGroupsUnavailable(Object):
    """
    The user can't be a member of a public supergroup

    Attributes:
        ID (:obj:`str`): ``CheckChatUsernameResultPublicGroupsUnavailable``

    No parameters required.

    Returns:
        CheckChatUsernameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkChatUsernameResultPublicGroupsUnavailable"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckChatUsernameResultPublicGroupsUnavailable":
        
        return CheckChatUsernameResultPublicGroupsUnavailable()
