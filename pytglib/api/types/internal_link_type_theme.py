

from ..utils import Object


class InternalLinkTypeTheme(Object):
    """
    The link is a link to a theme. TDLib has no theme support yet 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeTheme``

    Args:
        theme_name (:obj:`str`):
            Name of the theme

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeTheme"

    def __init__(self, theme_name, **kwargs):
        
        self.theme_name = theme_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeTheme":
        theme_name = q.get('theme_name')
        return InternalLinkTypeTheme(theme_name)
