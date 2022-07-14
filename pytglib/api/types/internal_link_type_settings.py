

from ..utils import Object


class InternalLinkTypeSettings(Object):
    """
    The link is a link to application settings

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeSettings``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeSettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeSettings":
        
        return InternalLinkTypeSettings()
