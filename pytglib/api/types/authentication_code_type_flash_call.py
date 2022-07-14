

from ..utils import Object


class AuthenticationCodeTypeFlashCall(Object):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The phone number that calls is the code that must be entered automatically 

    Attributes:
        ID (:obj:`str`): ``AuthenticationCodeTypeFlashCall``

    Args:
        pattern (:obj:`str`):
            Pattern of the phone number from which the call will be made

    Returns:
        AuthenticationCodeType

    Raises:
        :class:`telegram.Error`
    """
    ID = "authenticationCodeTypeFlashCall"

    def __init__(self, pattern, **kwargs):
        
        self.pattern = pattern  # str

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeFlashCall":
        pattern = q.get('pattern')
        return AuthenticationCodeTypeFlashCall(pattern)
