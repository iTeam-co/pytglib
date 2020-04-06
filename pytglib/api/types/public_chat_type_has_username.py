

from ..utils import Object


class PublicChatTypeHasUsername(Object):
    """
    The chat is public, because it has username

    Attributes:
        ID (:obj:`str`): ``PublicChatTypeHasUsername``

    No parameters required.

    Returns:
        PublicChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "publicChatTypeHasUsername"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PublicChatTypeHasUsername":
        
        return PublicChatTypeHasUsername()
