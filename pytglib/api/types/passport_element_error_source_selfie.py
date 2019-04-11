

from ..utils import Object


class PassportElementErrorSourceSelfie(Object):
    """
    The selfie with the document contains an error. The error will be considered resolved when the file with the selfie changes

    Attributes:
        ID (:obj:`str`): ``PassportElementErrorSourceSelfie``

    No parameters required.

    Returns:
        PassportElementErrorSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementErrorSourceSelfie"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementErrorSourceSelfie":
        
        return PassportElementErrorSourceSelfie()
