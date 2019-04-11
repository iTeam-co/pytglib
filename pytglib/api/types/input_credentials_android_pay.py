

from ..utils import Object


class InputCredentialsAndroidPay(Object):
    """
    Applies if a user enters new credentials using Android Pay 

    Attributes:
        ID (:obj:`str`): ``InputCredentialsAndroidPay``

    Args:
        data (:obj:`str`):
            JSON-encoded data with the credential identifier

    Returns:
        InputCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputCredentialsAndroidPay"

    def __init__(self, data, **kwargs):
        
        self.data = data  # str

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsAndroidPay":
        data = q.get('data')
        return InputCredentialsAndroidPay(data)
