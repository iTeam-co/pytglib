

from ..utils import Object


class CheckPhoneNumberConfirmationCode(Object):
    """
    Checks phone number confirmation code 

    Attributes:
        ID (:obj:`str`): ``CheckPhoneNumberConfirmationCode``

    Args:
        code (:obj:`str`):
            The phone number confirmation code

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkPhoneNumberConfirmationCode"

    def __init__(self, code, extra=None, **kwargs):
        self.extra = extra
        self.code = code  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckPhoneNumberConfirmationCode":
        code = q.get('code')
        return CheckPhoneNumberConfirmationCode(code)
