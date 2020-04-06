

from ..utils import Object


class SetStickerPositionInSet(Object):
    """
    Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

    Attributes:
        ID (:obj:`str`): ``SetStickerPositionInSet``

    Args:
        sticker (:class:`telegram.api.types.InputFile`):
            Sticker 
        position (:obj:`int`):
            New position of the sticker in the set, zero-based

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setStickerPositionInSet"

    def __init__(self, sticker, position, extra=None, **kwargs):
        self.extra = extra
        self.sticker = sticker  # InputFile
        self.position = position  # int

    @staticmethod
    def read(q: dict, *args) -> "SetStickerPositionInSet":
        sticker = Object.read(q.get('sticker'))
        position = q.get('position')
        return SetStickerPositionInSet(sticker, position)
