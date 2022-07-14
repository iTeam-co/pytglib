

from ..utils import Object


class GroupCallVideoQuality(Object):
    """
    Describes the quality of a group call video

    No parameters required.
    """
    ID = "groupCallVideoQuality"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "GroupCallVideoQualityMedium or GroupCallVideoQualityThumbnail or GroupCallVideoQualityFull":
        if q.get("@type"):
            return Object.read(q)
        return GroupCallVideoQuality()
