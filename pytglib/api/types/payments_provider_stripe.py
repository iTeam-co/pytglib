

from ..utils import Object


class PaymentsProviderStripe(Object):
    """
    Stripe payment provider 

    Attributes:
        ID (:obj:`str`): ``PaymentsProviderStripe``

    Args:
        publishable_key (:obj:`str`):
            Stripe API publishable key 
        need_country (:obj:`bool`):
            True, if the user country must be provided 
        need_postal_code (:obj:`bool`):
            True, if the user ZIP/postal code must be provided 
        need_cardholder_name (:obj:`bool`):
            True, if the cardholder name must be provided

    Returns:
        PaymentsProviderStripe

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentsProviderStripe"

    def __init__(self, publishable_key, need_country, need_postal_code, need_cardholder_name, **kwargs):
        
        self.publishable_key = publishable_key  # str
        self.need_country = need_country  # bool
        self.need_postal_code = need_postal_code  # bool
        self.need_cardholder_name = need_cardholder_name  # bool

    @staticmethod
    def read(q: dict, *args) -> "PaymentsProviderStripe":
        publishable_key = q.get('publishable_key')
        need_country = q.get('need_country')
        need_postal_code = q.get('need_postal_code')
        need_cardholder_name = q.get('need_cardholder_name')
        return PaymentsProviderStripe(publishable_key, need_country, need_postal_code, need_cardholder_name)
