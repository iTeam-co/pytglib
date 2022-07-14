

from ..utils import Object


class GetCountries(Object):
    """
    Returns information about existing countries. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetCountries``

    No parameters required.

    Returns:
        Countries

    Raises:
        :class:`telegram.Error`
    """
    ID = "getCountries"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetCountries":
        
        return GetCountries()
