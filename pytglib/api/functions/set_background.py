

from ..utils import Object


class SetBackground(Object):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds

    Attributes:
        ID (:obj:`str`): ``SetBackground``

    Args:
        background (:class:`telegram.api.types.InputBackground`):
            The input background to use, null for filled backgrounds
        type (:class:`telegram.api.types.BackgroundType`):
            Background type; null for default backgroundThe method will return error 404 if type is null
        for_dark_theme (:obj:`bool`):
            True, if the background is chosen for dark theme

    Returns:
        Background

    Raises:
        :class:`telegram.Error`
    """
    ID = "setBackground"

    def __init__(self, background, type, for_dark_theme, extra=None, **kwargs):
        self.extra = extra
        self.background = background  # InputBackground
        self.type = type  # BackgroundType
        self.for_dark_theme = for_dark_theme  # bool

    @staticmethod
    def read(q: dict, *args) -> "SetBackground":
        background = Object.read(q.get('background'))
        type = Object.read(q.get('type'))
        for_dark_theme = q.get('for_dark_theme')
        return SetBackground(background, type, for_dark_theme)
