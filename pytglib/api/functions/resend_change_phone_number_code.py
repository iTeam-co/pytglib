

from ..utils import Object


class ResendChangePhoneNumberCode(Object):
    """
    Re-sends the authentication code sent to confirm a new phone number for the current user. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed

    Attributes:
        ID (:obj:`str`): ``ResendChangePhoneNumberCode``

    No parameters required.

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendChangePhoneNumberCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendChangePhoneNumberCode":
        
        return ResendChangePhoneNumberCode()
