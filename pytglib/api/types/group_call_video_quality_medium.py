

from ..utils import Object


class GroupCallVideoQualityMedium(Object):
    """
    The medium video quality

    Attributes:
        ID (:obj:`str`): ``GroupCallVideoQualityMedium``

    No parameters required.

    Returns:
        GroupCallVideoQuality

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallVideoQualityMedium"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "GroupCallVideoQualityMedium":
        
        return GroupCallVideoQualityMedium()
