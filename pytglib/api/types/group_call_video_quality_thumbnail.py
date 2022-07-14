

from ..utils import Object


class GroupCallVideoQualityThumbnail(Object):
    """
    The worst available video quality

    Attributes:
        ID (:obj:`str`): ``GroupCallVideoQualityThumbnail``

    No parameters required.

    Returns:
        GroupCallVideoQuality

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallVideoQualityThumbnail"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "GroupCallVideoQualityThumbnail":
        
        return GroupCallVideoQualityThumbnail()
