

from ..utils import Object


class CheckAuthenticationPassword(Object):
    """
    Checks the authentication password for correctness. Works only when the current authorization state is authorizationStateWaitPassword 

    Attributes:
        ID (:obj:`str`): ``CheckAuthenticationPassword``

    Args:
        password (:obj:`str`):
            The password to check

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkAuthenticationPassword"

    def __init__(self, password, extra=None, **kwargs):
        self.extra = extra
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckAuthenticationPassword":
        password = q.get('password')
        return CheckAuthenticationPassword(password)
