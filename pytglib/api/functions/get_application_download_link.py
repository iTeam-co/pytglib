

from ..utils import Object


class GetApplicationDownloadLink(Object):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram

    Attributes:
        ID (:obj:`str`): ``GetApplicationDownloadLink``

    No parameters required.

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getApplicationDownloadLink"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetApplicationDownloadLink":
        
        return GetApplicationDownloadLink()
