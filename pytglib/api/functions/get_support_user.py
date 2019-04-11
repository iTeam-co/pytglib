

from ..utils import Object


class GetSupportUser(Object):
    """
    Returns a user that can be contacted to get support

    Attributes:
        ID (:obj:`str`): ``GetSupportUser``

    No parameters required.

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSupportUser"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetSupportUser":
        
        return GetSupportUser()
