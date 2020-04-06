

from ..utils import Object


class GetBackgrounds(Object):
    """
    Returns backgrounds installed by the user 

    Attributes:
        ID (:obj:`str`): ``GetBackgrounds``

    Args:
        for_dark_theme (:obj:`bool`):
            True, if the backgrounds needs to be ordered for dark theme

    Returns:
        Backgrounds

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBackgrounds"

    def __init__(self, for_dark_theme, extra=None, **kwargs):
        self.extra = extra
        self.for_dark_theme = for_dark_theme  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetBackgrounds":
        for_dark_theme = q.get('for_dark_theme')
        return GetBackgrounds(for_dark_theme)
