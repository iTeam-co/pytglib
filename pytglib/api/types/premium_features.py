

from ..utils import Object


class PremiumFeatures(Object):
    """
    Contains information about features, available to Premium users 

    Attributes:
        ID (:obj:`str`): ``PremiumFeatures``

    Args:
        features (List of :class:`telegram.api.types.PremiumFeature`):
            The list of available features 
        limits (List of :class:`telegram.api.types.premiumLimit`):
            The list of limits, increased for Premium users
        payment_link (:class:`telegram.api.types.InternalLinkType`):
            An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available

    Returns:
        PremiumFeatures

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumFeatures"

    def __init__(self, features, limits, payment_link, **kwargs):
        
        self.features = features  # list of PremiumFeature
        self.limits = limits  # list of premiumLimit
        self.payment_link = payment_link  # InternalLinkType

    @staticmethod
    def read(q: dict, *args) -> "PremiumFeatures":
        features = [Object.read(i) for i in q.get('features', [])]
        limits = [Object.read(i) for i in q.get('limits', [])]
        payment_link = Object.read(q.get('payment_link'))
        return PremiumFeatures(features, limits, payment_link)
