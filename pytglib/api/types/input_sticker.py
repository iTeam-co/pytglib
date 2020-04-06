

from ..utils import Object


class InputSticker(Object):
    """
    Describes a sticker that needs to be added to a sticker set

    No parameters required.
    """
    ID = "inputSticker"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputStickerAnimated or InputStickerStatic":
        if q.get("@type"):
            return Object.read(q)
        return InputSticker()
