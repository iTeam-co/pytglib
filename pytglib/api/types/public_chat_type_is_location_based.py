

from ..utils import Object


class PublicChatTypeIsLocationBased(Object):
    """
    The chat is public, because it is a location-based supergroup

    Attributes:
        ID (:obj:`str`): ``PublicChatTypeIsLocationBased``

    No parameters required.

    Returns:
        PublicChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "publicChatTypeIsLocationBased"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PublicChatTypeIsLocationBased":
        
        return PublicChatTypeIsLocationBased()
