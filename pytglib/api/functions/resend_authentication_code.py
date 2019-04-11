

from ..utils import Object


class ResendAuthenticationCode(Object):
    """
    Re-sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode and the next_code_type of the result is not null

    Attributes:
        ID (:obj:`str`): ``ResendAuthenticationCode``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "resendAuthenticationCode"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResendAuthenticationCode":
        
        return ResendAuthenticationCode()
