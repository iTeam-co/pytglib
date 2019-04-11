

from ..utils import Object


class AuthenticationCodeInfo(Object):
    """
    Information about the authentication code that was sent 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeInfo``

    Args:
        phone_number (:obj:`str`):
            A phone number that is being authenticated 
        type (:class:`telegram.api.types.AuthenticationCodeType`):
            Describes the way the code was sent to the user 
        next_type (:class:`telegram.api.types.AuthenticationCodeType`):
            Describes the way the next code will be sent to the user; may be null 
        timeout (:obj:`int`):
            Timeout before the code should be re-sent, in seconds

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeInfo"

    def __init__(self, phone_number, type, next_type, timeout, **kwargs):
        
        self.phone_number = phone_number  # str
        self.type = type  # AuthenticationCodeType
        self.next_type = next_type  # AuthenticationCodeType
        self.timeout = timeout  # int

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeInfo":
        phone_number = q.get('phone_number')
        type = Object.read(q.get('type'))
        next_type = Object.read(q.get('next_type'))
        timeout = q.get('timeout')
        return AuthenticationCodeInfo(phone_number, type, next_type, timeout)
