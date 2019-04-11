

from ..utils import Object


class CreateTemporaryPassword(Object):
    """
    Creates a new temporary password for processing payments 

    Attributes:
        ID (:obj:`str`): ``CreateTemporaryPassword``

    Args:
        password (:obj:`str`):
            Persistent user password 
        valid_for (:obj:`int`):
            Time during which the temporary password will be valid, in seconds; should be between 60 and 86400

    Returns:
        TemporaryPasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "createTemporaryPassword"

    def __init__(self, password, valid_for, extra=None, **kwargs):
        self.extra = extra
        self.password = password  # str
        self.valid_for = valid_for  # int

    @staticmethod
    def read(q: dict, *args) -> "CreateTemporaryPassword":
        password = q.get('password')
        valid_for = q.get('valid_for')
        return CreateTemporaryPassword(password, valid_for)
