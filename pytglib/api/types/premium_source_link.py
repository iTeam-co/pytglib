

from ..utils import Object


class PremiumSourceLink(Object):
    """
    A user opened an internal link of the type internalLinkTypePremiumFeatures 

    Attributes:
        ID (:obj:`str`): ``PremiumSourceLink``

    Args:
        referrer (:obj:`str`):
            The referrer from the link

    Returns:
        PremiumSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumSourceLink"

    def __init__(self, referrer, **kwargs):
        
        self.referrer = referrer  # str

    @staticmethod
    def read(q: dict, *args) -> "PremiumSourceLink":
        referrer = q.get('referrer')
        return PremiumSourceLink(referrer)
