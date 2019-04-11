

from ..utils import Object


class Invoice(Object):
    """
    Product invoice 

    Attributes:
        ID (:obj:`str`): ``Invoice``

    Args:
        currency (:obj:`str`):
            ISO 4217 currency code 
        price_parts (List of :class:`telegram.api.types.labeledPricePart`):
            A list of objects used to calculate the total price of the product 
        is_test (:obj:`bool`):
            True, if the payment is a test payment
        need_name (:obj:`bool`):
            True, if the user's name is needed for payment 
        need_phone_number (:obj:`bool`):
            True, if the user's phone number is needed for payment 
        need_email_address (:obj:`bool`):
            True, if the user's email address is needed for payment
        need_shipping_address (:obj:`bool`):
            True, if the user's shipping address is needed for payment 
        send_phone_number_to_provider (:obj:`bool`):
            True, if the user's phone number will be sent to the provider
        send_email_address_to_provider (:obj:`bool`):
            True, if the user's email address will be sent to the provider 
        is_flexible (:obj:`bool`):
            True, if the total price depends on the shipping method

    Returns:
        Invoice

    Raises:
        :class:`telegram.Error`
    """
    ID = "invoice"

    def __init__(self, currency, price_parts, is_test, need_name, need_phone_number, need_email_address, need_shipping_address, send_phone_number_to_provider, send_email_address_to_provider, is_flexible, **kwargs):
        
        self.currency = currency  # str
        self.price_parts = price_parts  # list of labeledPricePart
        self.is_test = is_test  # bool
        self.need_name = need_name  # bool
        self.need_phone_number = need_phone_number  # bool
        self.need_email_address = need_email_address  # bool
        self.need_shipping_address = need_shipping_address  # bool
        self.send_phone_number_to_provider = send_phone_number_to_provider  # bool
        self.send_email_address_to_provider = send_email_address_to_provider  # bool
        self.is_flexible = is_flexible  # bool

    @staticmethod
    def read(q: dict, *args) -> "Invoice":
        currency = q.get('currency')
        price_parts = [Object.read(i) for i in q.get('price_parts', [])]
        is_test = q.get('is_test')
        need_name = q.get('need_name')
        need_phone_number = q.get('need_phone_number')
        need_email_address = q.get('need_email_address')
        need_shipping_address = q.get('need_shipping_address')
        send_phone_number_to_provider = q.get('send_phone_number_to_provider')
        send_email_address_to_provider = q.get('send_email_address_to_provider')
        is_flexible = q.get('is_flexible')
        return Invoice(currency, price_parts, is_test, need_name, need_phone_number, need_email_address, need_shipping_address, send_phone_number_to_provider, send_email_address_to_provider, is_flexible)
