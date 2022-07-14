

from ..utils import Object


class GetThemeParametersJsonString(Object):
    """
    Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetThemeParametersJsonString``

    Args:
        theme (:class:`telegram.api.types.themeParameters`):
            Theme parameters to convert to JSON

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getThemeParametersJsonString"

    def __init__(self, theme, extra=None, **kwargs):
        self.extra = extra
        self.theme = theme  # ThemeParameters

    @staticmethod
    def read(q: dict, *args) -> "GetThemeParametersJsonString":
        theme = Object.read(q.get('theme'))
        return GetThemeParametersJsonString(theme)
