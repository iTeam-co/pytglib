

from ..utils import Object


class GetSavedAnimations(Object):
    """
    Returns saved animations

    Attributes:
        ID (:obj:`str`): ``GetSavedAnimations``

    No parameters required.

    Returns:
        Animations

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSavedAnimations"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetSavedAnimations":
        
        return GetSavedAnimations()
