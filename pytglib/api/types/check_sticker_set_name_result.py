

from ..utils import Object


class CheckStickerSetNameResult(Object):
    """
    Represents result of checking whether a name can be used for a new sticker set

    No parameters required.
    """
    ID = "checkStickerSetNameResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckStickerSetNameResultOk or CheckStickerSetNameResultNameOccupied or CheckStickerSetNameResultNameInvalid":
        if q.get("@type"):
            return Object.read(q)
        return CheckStickerSetNameResult()
