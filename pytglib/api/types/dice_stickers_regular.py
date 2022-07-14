

from ..utils import Object


class DiceStickersRegular(Object):
    """
    A regular animated sticker 

    Attributes:
        ID (:obj:`str`): ``DiceStickersRegular``

    Args:
        sticker (:class:`telegram.api.types.sticker`):
            The animated sticker with the dice animation

    Returns:
        DiceStickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "diceStickersRegular"

    def __init__(self, sticker, **kwargs):
        
        self.sticker = sticker  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "DiceStickersRegular":
        sticker = Object.read(q.get('sticker'))
        return DiceStickersRegular(sticker)
