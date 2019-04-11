

from ..utils import Object


class PassportElementErrorSourceFiles(Object):
    """
    The list of attached files contains an error. The error will be considered resolved when the list of files changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceFiles``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceFiles"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceFiles":
        
        return PassportElementErrorSourceFiles()
