

from ..utils import Object


class PremiumState(Object):
    """
    Contains state of Telegram Premium subscription and promotion videos for Premium features

    Attributes:
        ID (:obj:`str`): ``PremiumState``

    Args:
        state (:class:`telegram.api.types.formattedText`):
            Text description of the state of the current Premium subscription; may be empty if the current user has no Telegram Premium subscription
        currency (:obj:`str`):
            ISO 4217 currency code for Telegram Premium subscription payment
        monthly_amount (:obj:`int`):
            Monthly subscription payment for Telegram Premium subscription, in the smallest units of the currency
        animations (List of :class:`telegram.api.types.premiumFeaturePromotionAnimation`):
            The list of available promotion animations for Premium features

    Returns:
        PremiumState

    Raises:
        :class:`telegram.Error`
    """
    ID = "premiumState"

    def __init__(self, state, currency, monthly_amount, animations, **kwargs):
        
        self.state = state  # FormattedText
        self.currency = currency  # str
        self.monthly_amount = monthly_amount  # int
        self.animations = animations  # list of premiumFeaturePromotionAnimation

    @staticmethod
    def read(q: dict, *args) -> "PremiumState":
        state = Object.read(q.get('state'))
        currency = q.get('currency')
        monthly_amount = q.get('monthly_amount')
        animations = [Object.read(i) for i in q.get('animations', [])]
        return PremiumState(state, currency, monthly_amount, animations)
