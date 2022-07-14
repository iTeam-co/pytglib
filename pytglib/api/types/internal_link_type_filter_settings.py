

from ..utils import Object


class InternalLinkTypeFilterSettings(Object):
    """
    The link is a link to the filter settings section of the app

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeFilterSettings``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeFilterSettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeFilterSettings":
        
        return InternalLinkTypeFilterSettings()
