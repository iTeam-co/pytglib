

from ..utils import Object


class GetExternalLink(Object):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

    Attributes:
        ID (:obj:`str`): ``GetExternalLink``

    Args:
        link (:obj:`str`):
            The HTTP link 
        allow_write_access (:obj:`bool`):
            Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getExternalLink"

    def __init__(self, link, allow_write_access, extra=None, **kwargs):
        self.extra = extra
        self.link = link  # str
        self.allow_write_access = allow_write_access  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetExternalLink":
        link = q.get('link')
        allow_write_access = q.get('allow_write_access')
        return GetExternalLink(link, allow_write_access)
