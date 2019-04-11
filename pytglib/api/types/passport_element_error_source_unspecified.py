

from ..utils import Object


class PassportElementErrorSourceUnspecified(Object):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceUnspecified``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceUnspecified"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceUnspecified":
        
        return PassportElementErrorSourceUnspecified()
