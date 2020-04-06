

from ..utils import Object


class UpdateSelectedBackground(Object):
    """
    The selected background has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateSelectedBackground``

    Args:
        for_dark_theme (:obj:`bool`):
            True, if background for dark theme has changed 
        background (:class:`telegram.api.types.background`):
            The new selected background; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSelectedBackground"

    def __init__(self, for_dark_theme, background, **kwargs):
        
        self.for_dark_theme = for_dark_theme  # bool
        self.background = background  # Background

    @staticmethod
    def read(q: dict, *args) -> "UpdateSelectedBackground":
        for_dark_theme = q.get('for_dark_theme')
        background = Object.read(q.get('background'))
        return UpdateSelectedBackground(for_dark_theme, background)
