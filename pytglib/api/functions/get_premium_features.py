

from ..utils import Object


class GetPremiumFeatures(Object):
    """
    Returns information about features, available to Premium users 

    Attributes:
        ID (:obj:`str`): ``GetPremiumFeatures``

    Args:
        source (:class:`telegram.api.types.PremiumSource`):
            Source of the request; pass null if the method is called from some non-standard source

    Returns:
        PremiumFeatures

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPremiumFeatures"

    def __init__(self, source, extra=None, **kwargs):
        self.extra = extra
        self.source = source  # PremiumSource

    @staticmethod
    def read(q: dict, *args) -> "GetPremiumFeatures":
        source = Object.read(q.get('source'))
        return GetPremiumFeatures(source)
