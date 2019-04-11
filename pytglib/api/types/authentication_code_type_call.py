

from ..utils import Object


class AuthenticationCodeTypeCall(Object):
    """
    An authentication code is delivered via a phone call to the specified phone number 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeTypeCall``

    Args:
        length (:obj:`int`):
            Length of the code

    Returns:
        AuthenticationCodeType

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeTypeCall"

    def __init__(self, length, **kwargs):
        
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeCall":
        length = q.get('length')
        return AuthenticationCodeTypeCall(length)
