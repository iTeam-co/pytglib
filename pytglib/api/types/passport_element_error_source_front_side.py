

from ..utils import Object


class PassportElementErrorSourceFrontSide(Object):
    """
    The front side of the document contains an error. The error will be considered resolved when the file with the front side changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceFrontSide``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceFrontSide"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceFrontSide":
        
        return PassportElementErrorSourceFrontSide()
