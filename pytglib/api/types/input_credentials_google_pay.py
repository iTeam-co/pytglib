

from ..utils import Object


class InputCredentialsGooglePay(Object):
    """
    Applies if a user enters new credentials using Google Pay 

    Attributes:
        ID (:obj:`str`): ``InputCredentialsGooglePay``

    Args:
        data (:obj:`str`):
            JSON-encoded data with the credential identifier

    Returns:
        InputCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputCredentialsGooglePay"

    def __init__(self, data, **kwargs):
        
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsGooglePay":
        data = q.get('data')
        return InputCredentialsGooglePay(data)
