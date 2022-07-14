

from ..utils import Object


class InternalLinkTypeThemeSettings(Object):
    """
    The link is a link to the theme settings section of the app

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeThemeSettings``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeThemeSettings"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeThemeSettings":
        
        return InternalLinkTypeThemeSettings()
