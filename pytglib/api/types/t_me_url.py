

from ..utils import Object


class TMeUrl(Object):
    """
    Represents a URL linking to an internal Telegram entity 

    Attributes:
        ID (:obj:`str`): ``TMeUrl``

    Args:
        url (:obj:`str`):
            URL 
        type (:class:`telegram.api.types.TMeUrlType`):
            Type of the URL

    Returns:
        TMeUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrl"

    def __init__(self, url, type, **kwargs):
        
        self.url = url  # str
        self.type = type  # TMeUrlType

    @staticmethod
    def read(q: dict, *args) -> "TMeUrl":
        url = q.get('url')
        type = Object.read(q.get('type'))
        return TMeUrl(url, type)
