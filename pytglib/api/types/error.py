

from ..utils import Object


class Error(Object):
    """
    An object of this type can be returned on every function call, in case of an error

    Attributes:
        ID (:obj:`str`): ``Error``

    Args:
        code (:obj:`int`):
            Error code; subject to future changesIf the error code is 406, the error message must not be processed in any way and must not be displayed to the user
        message (:obj:`str`):
            Error message; subject to future changes

    Returns:
        Error

    Raises:
        :class:`telegram.Error`
    """
    ID = "error"

    def __init__(self, code, message, **kwargs):
        
        self.code = code  # int
        self.message = message  # str

    @staticmethod
    def read(q: dict, *args) -> "Error":
        code = q.get('code')
        message = q.get('message')
        return Error(code, message)
