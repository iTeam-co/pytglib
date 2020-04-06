

from ..utils import Object


class GetBackgroundUrl(Object):
    """
    Constructs a persistent HTTP URL for a background 

    Attributes:
        ID (:obj:`str`): ``GetBackgroundUrl``

    Args:
        name (:obj:`str`):
            Background name 
        type (:class:`telegram.api.types.BackgroundType`):
            Background type

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getBackgroundUrl"

    def __init__(self, name, type, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str
        self.type = type  # BackgroundType

    @staticmethod
    def read(q: dict, *args) -> "GetBackgroundUrl":
        name = q.get('name')
        type = Object.read(q.get('type'))
        return GetBackgroundUrl(name, type)
