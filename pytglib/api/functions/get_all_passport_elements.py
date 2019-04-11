

from ..utils import Object


class GetAllPassportElements(Object):
    """
    Returns all available Telegram Passport elements 

    Attributes:
        ID (:obj:`str`): ``GetAllPassportElements``

    Args:
        password (:obj:`str`):
            Password of the current user

    Returns:
        PassportElements

    Raises:
        :class:`telegram.Error`
    """
    ID = "getAllPassportElements"

    def __init__(self, password, extra=None, **kwargs):
        self.extra = extra
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "GetAllPassportElements":
        password = q.get('password')
        return GetAllPassportElements(password)
