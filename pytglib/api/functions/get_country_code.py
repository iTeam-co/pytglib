

from ..utils import Object


class GetCountryCode(Object):
    """
    Uses current user IP to found their country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetCountryCode``

    No parameters required.

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCountryCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetCountryCode":
        
        return GetCountryCode()
