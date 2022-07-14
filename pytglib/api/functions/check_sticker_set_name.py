

from ..utils import Object


class CheckStickerSetName(Object):
    """
    Checks whether a name can be used for a new sticker set 

    Attributes:
        ID (:obj:`str`): ``CheckStickerSetName``

    Args:
        name (:obj:`str`):
            Name to be checked

    Returns:
        CheckStickerSetNameResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "checkStickerSetName"

    def __init__(self, name, extra=None, **kwargs):
        self.extra = extra
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "CheckStickerSetName":
        name = q.get('name')
        return CheckStickerSetName(name)
