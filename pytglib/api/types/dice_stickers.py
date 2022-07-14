

from ..utils import Object


class DiceStickers(Object):
    """
    Contains animated stickers which must be used for dice animation rendering

    No parameters required.
    """
    ID = "diceStickers"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "DiceStickersSlotMachine or DiceStickersRegular":
        if q.get("@type"):
            return Object.read(q)
        return DiceStickers()
