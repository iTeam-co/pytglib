

from ..utils import Object


class InternalLinkTypePremiumFeatures(Object):
    """
    The link is a link to the Premium features screen of the applcation from which the user can subscribe to Telegram Premium. Call getPremiumFeatures with the given referrer to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypePremiumFeatures``

    Args:
        referrer (:obj:`str`):
            Referrer specified in the link

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypePremiumFeatures"

    def __init__(self, referrer, **kwargs):
        
        self.referrer = referrer  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypePremiumFeatures":
        referrer = q.get('referrer')
        return InternalLinkTypePremiumFeatures(referrer)
