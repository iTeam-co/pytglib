

from ..utils import Object


class CheckStickerSetNameResultOk(Object):
    """
    The name can be set

    Attributes:
        ID (:obj:`str`): ``CheckStickerSetNameResultOk``

    No parameters required.

    Returns:
        CheckStickerSetNameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkStickerSetNameResultOk"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckStickerSetNameResultOk":
        
        return CheckStickerSetNameResultOk()
