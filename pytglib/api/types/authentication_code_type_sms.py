

from ..utils import Object


class AuthenticationCodeTypeSms(Object):
    """
    An authentication code is delivered via an SMS message to the specified phone number 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeTypeSms``

    Args:
        length (:obj:`int`):
            Length of the code

    Returns:
        AuthenticationCodeType

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeTypeSms"

    def __init__(self, length, **kwargs):
        
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeSms":
        length = q.get('length')
        return AuthenticationCodeTypeSms(length)
