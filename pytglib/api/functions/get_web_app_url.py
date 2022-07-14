

from ..utils import Object


class GetWebAppUrl(Object):
    """
    Returns an HTTPS URL of a Web App to open after keyboardButtonTypeWebApp button is pressed

    Attributes:
        ID (:obj:`str`): ``GetWebAppUrl``

    Args:
        bot_user_id (:obj:`int`):
            Identifier of the target bot
        url (:obj:`str`):
            The URL from the keyboardButtonTypeWebApp button
        theme (:class:`telegram.api.types.themeParameters`):
            Preferred Web App theme; pass null to use the default theme

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getWebAppUrl"

    def __init__(self, bot_user_id, url, theme, extra=None, **kwargs):
        self.extra = extra
        self.bot_user_id = bot_user_id  # int
        self.url = url  # str
        self.theme = theme  # ThemeParameters

    @staticmethod
    def read(q: dict, *args) -> "GetWebAppUrl":
        bot_user_id = q.get('bot_user_id')
        url = q.get('url')
        theme = Object.read(q.get('theme'))
        return GetWebAppUrl(bot_user_id, url, theme)
