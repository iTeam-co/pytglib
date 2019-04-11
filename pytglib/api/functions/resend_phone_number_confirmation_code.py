

from ..utils import Object


class ResendPhoneNumberConfirmationCode(Object):
    """
    Resends phone number confirmation code

    Attributes:
        ID (:obj:`str`): ``ResendPhoneNumberConfirmationCode``

    No parameters required.

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendPhoneNumberConfirmationCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendPhoneNumberConfirmationCode":
        
        return ResendPhoneNumberConfirmationCode()
