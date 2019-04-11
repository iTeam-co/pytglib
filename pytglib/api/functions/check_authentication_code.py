

from ..utils import Object


class CheckAuthenticationCode(Object):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode 

    Attributes:
        ID (:obj:`str`): ``CheckAuthenticationCode``

    Args:
        code (:obj:`str`):
            The verification code received via SMS, Telegram message, phone call, or flash call
        first_name (:obj:`str`):
            If the user is not yet registered, the first name of the user; 1-255 characters 
        last_name (:obj:`str`):
            If the user is not yet registered; the last name of the user; optional; 0-255 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkAuthenticationCode"

    def __init__(self, code, first_name, last_name, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str
        self.first_name = first_name  # str
        self.last_name = last_name  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckAuthenticationCode":
        code = q.get('code')
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        return CheckAuthenticationCode(code, first_name, last_name)
