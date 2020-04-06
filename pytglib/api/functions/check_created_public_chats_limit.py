

from ..utils import Object


class CheckCreatedPublicChatsLimit(Object):
    """
    Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached 

    Attributes:
        ID (:obj:`str`): ``CheckCreatedPublicChatsLimit``

    Args:
        type (:class:`telegram.api.types.PublicChatType`):
            Type of the public chats, for which to check the limit

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkCreatedPublicChatsLimit"

    def __init__(self, type, extra=None, **kwargs):
        self.extra = extra
        self.type = type  # PublicChatType

    @staticmethod
    def read(q: dict, *args) -> "CheckCreatedPublicChatsLimit":
        type = Object.read(q.get('type'))
        return CheckCreatedPublicChatsLimit(type)
