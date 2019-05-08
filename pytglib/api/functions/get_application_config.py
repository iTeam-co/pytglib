

from ..utils import Object


class GetApplicationConfig(Object):
    """
    Returns application config, provided by the server. Can be called before authorization

    Attributes:
        ID (:obj:`str`): ``GetApplicationConfig``

    No parameters required.

    Returns:
        JsonValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "getApplicationConfig"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetApplicationConfig":
        
        return GetApplicationConfig()
