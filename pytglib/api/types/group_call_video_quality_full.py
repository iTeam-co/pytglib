

from ..utils import Object


class GroupCallVideoQualityFull(Object):
    """
    The best available video quality

    Attributes:
        ID (:obj:`str`): ``GroupCallVideoQualityFull``

    No parameters required.

    Returns:
        GroupCallVideoQuality

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallVideoQualityFull"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "GroupCallVideoQualityFull":
        
        return GroupCallVideoQualityFull()
