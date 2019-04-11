

from ..utils import Object


class PassportElementErrorSourceReverseSide(Object):
    """
    The reverse side of the document contains an error. The error will be considered resolved when the file with the reverse side changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceReverseSide``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceReverseSide"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceReverseSide":
        
        return PassportElementErrorSourceReverseSide()
