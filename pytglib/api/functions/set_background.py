

from ..utils import Object


class SetBackground(Object):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds

    Attributes:
        ID (:obj:`str`): ``SetBackground``

    Args:
        background (:class:`telegram.api.types.InputBackground`):
            The input background to use; pass null to create a new filled backgrounds or to remove the current background
        type (:class:`telegram.api.types.BackgroundType`):
            Background type; pass null to use the default type of the remote background or to remove the current background
        for_dark_theme (:obj:`bool`):
            Pass true if the background is changed for a dark theme

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
