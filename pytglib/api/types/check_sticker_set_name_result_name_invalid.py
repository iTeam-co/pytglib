

from ..utils import Object


class CheckStickerSetNameResultNameInvalid(Object):
    """
    The name is invalid

    Attributes:
        ID (:obj:`str`): ``CheckStickerSetNameResultNameInvalid``

    No parameters required.

    Returns:
        CheckStickerSetNameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkStickerSetNameResultNameInvalid"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckStickerSetNameResultNameInvalid":
        
        return CheckStickerSetNameResultNameInvalid()
