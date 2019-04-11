

from ..utils import Object


class PassportElementErrorSourceFile(Object):
    """
    The file contains an error. The error will be considered resolved when the file changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceFile``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceFile"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceFile":
        
        return PassportElementErrorSourceFile()
