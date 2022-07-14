

from ..utils import Object


class CheckStickerSetNameResultNameOccupied(Object):
    """
    The name is occupied

    Attributes:
        ID (:obj:`str`): ``CheckStickerSetNameResultNameOccupied``

    No parameters required.

    Returns:
        CheckStickerSetNameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkStickerSetNameResultNameOccupied"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "CheckStickerSetNameResultNameOccupied":
        
        return CheckStickerSetNameResultNameOccupied()
