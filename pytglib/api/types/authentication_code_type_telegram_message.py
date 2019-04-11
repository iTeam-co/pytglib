

from ..utils import Object


class AuthenticationCodeTypeTelegramMessage(Object):
    """
    An authentication code is delivered via a private Telegram message, which can be viewed in another client 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeTypeTelegramMessage``

    Args:
        length (:obj:`int`):
            Length of the code

    Returns:
        AuthenticationCodeType

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeTypeTelegramMessage"

    def __init__(self, length, **kwargs):
        
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeTelegramMessage":
        length = q.get('length')
        return AuthenticationCodeTypeTelegramMessage(length)
