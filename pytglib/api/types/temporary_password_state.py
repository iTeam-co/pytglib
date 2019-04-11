

from ..utils import Object


class TemporaryPasswordState(Object):
    """
    Returns information about the availability of a temporary password, which can be used for payments 

    Attributes:
        ID (:obj:`str`): ``TemporaryPasswordState``

    Args:
        has_password (:obj:`bool`):
            True, if a temporary password is available 
        valid_for (:obj:`int`):
            Time left before the temporary password expires, in seconds

    Returns:
        TemporaryPasswordState

    Raises:
        :class:`telegram.Error`
    """
    ID = "temporaryPasswordState"

    def __init__(self, has_password, valid_for, **kwargs):
        
        self.has_password = has_password  # bool
        self.valid_for = valid_for  # int

    @staticmethod
    def read(q: dict, *args) -> "TemporaryPasswordState":
        has_password = q.get('has_password')
        valid_for = q.get('valid_for')
        return TemporaryPasswordState(has_password, valid_for)
