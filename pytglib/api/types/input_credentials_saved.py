

from ..utils import Object


class InputCredentialsSaved(Object):
    """
    Applies if a user chooses some previously saved payment credentials. To use their previously saved credentials, the user must have a valid temporary password 

    Attributes:
        ID (:obj:`str`): ``InputCredentialsSaved``

    Args:
        saved_credentials_id (:obj:`str`):
            Identifier of the saved credentials

    Returns:
        InputCredentials

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputCredentialsSaved"

    def __init__(self, saved_credentials_id, **kwargs):
        
        self.saved_credentials_id = saved_credentials_id  # str

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsSaved":
        saved_credentials_id = q.get('saved_credentials_id')
        return InputCredentialsSaved(saved_credentials_id)
