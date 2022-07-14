

from ..utils import Object


class DiceStickersSlotMachine(Object):
    """
    Animated stickers to be combined into a slot machine

    Attributes:
        ID (:obj:`str`): ``DiceStickersSlotMachine``

    Args:
        background (:class:`telegram.api.types.sticker`):
            The animated sticker with the slot machine backgroundThe background animation must start playing after all reel animations finish
        lever (:class:`telegram.api.types.sticker`):
            The animated sticker with the lever animationThe lever animation must play once in the initial dice state
        left_reel (:class:`telegram.api.types.sticker`):
            The animated sticker with the left reel
        center_reel (:class:`telegram.api.types.sticker`):
            The animated sticker with the center reel
        right_reel (:class:`telegram.api.types.sticker`):
            The animated sticker with the right reel

    Returns:
        DiceStickers

    Raises:
        :class:`telegram.Error`
    """
    ID = "diceStickersSlotMachine"

    def __init__(self, background, lever, left_reel, center_reel, right_reel, **kwargs):
        
        self.background = background  # Sticker
        self.lever = lever  # Sticker
        self.left_reel = left_reel  # Sticker
        self.center_reel = center_reel  # Sticker
        self.right_reel = right_reel  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "DiceStickersSlotMachine":
        background = Object.read(q.get('background'))
        lever = Object.read(q.get('lever'))
        left_reel = Object.read(q.get('left_reel'))
        center_reel = Object.read(q.get('center_reel'))
        right_reel = Object.read(q.get('right_reel'))
        return DiceStickersSlotMachine(background, lever, left_reel, center_reel, right_reel)
