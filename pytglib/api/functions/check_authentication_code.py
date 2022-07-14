

from ..utils import Object


class CheckAuthenticationCode(Object):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode 

    Attributes:
        ID (:obj:`str`): ``CheckAuthenticationCode``

    Args:
        code (:obj:`str`):
            Authentication code to check

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkAuthenticationCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckAuthenticationCode":
        code = q.get('code')
        return CheckAuthenticationCode(code)
