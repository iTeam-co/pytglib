

from ..utils import Object


class ResetBackgrounds(Object):
    """
    Resets list of installed backgrounds to its default value

    Attributes:
        ID (:obj:`str`): ``ResetBackgrounds``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "resetBackgrounds"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ResetBackgrounds":
        
        return ResetBackgrounds()
