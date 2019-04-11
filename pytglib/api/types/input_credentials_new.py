

from ..utils import Object


class InputCredentialsNew(Object):
    """
    Applies if a user enters new credentials on a payment provider website 

    Attributes:
        ID (:obj:`str`): ``InputCredentialsNew``

    Args:
        data (:obj:`str`):
            Contains JSON-encoded data with a credential identifier from the payment provider 
        allow_save (:obj:`bool`):
            True, if the credential identifier can be saved on the server side

    Returns:
        InputCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputCredentialsNew"

    def __init__(self, data, allow_save, **kwargs):
        
        self.data = data  # str
        self.allow_save = allow_save  # bool

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsNew":
        data = q.get('data')
        allow_save = q.get('allow_save')
        return InputCredentialsNew(data, allow_save)
