

from ..utils import Object


class InputCredentialsApplePay(Object):
    """
    Applies if a user enters new credentials using Apple Pay 

    Attributes:
        ID (:obj:`str`): ``InputCredentialsApplePay``

    Args:
        data (:obj:`str`):
            JSON-encoded data with the credential identifier

    Returns:
        InputCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputCredentialsApplePay"

    def __init__(self, data, **kwargs):
        
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsApplePay":
        data = q.get('data')
        return InputCredentialsApplePay(data)
