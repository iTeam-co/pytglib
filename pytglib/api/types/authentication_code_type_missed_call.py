

from ..utils import Object


class AuthenticationCodeTypeMissedCall(Object):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The last digits of the phone number that calls are the code that must be entered manually by the user 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeTypeMissedCall``

    Args:
        phone_number_prefix (:obj:`str`):
            Prefix of the phone number from which the call will be made 
        length (:obj:`int`):
            Number of digits in the code, excluding the prefix

    Returns:
        AuthenticationCodeType

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeTypeMissedCall"

    def __init__(self, phone_number_prefix, length, **kwargs):
        
        self.phone_number_prefix = phone_number_prefix  # str
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeMissedCall":
        phone_number_prefix = q.get('phone_number_prefix')
        length = q.get('length')
        return AuthenticationCodeTypeMissedCall(phone_number_prefix, length)
