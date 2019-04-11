

from ..utils import Object


class MessageInvoice(Object):
    """
    A message with an invoice from a bot 

    Attributes:
        ID (:obj:`str`): ``MessageInvoice``

    Args:
        title (:obj:`str`):
            Product title 
        description (:obj:`str`):
            Product description 
        photo (:class:`telegram.api.types.photo`):
            Product photo; may be null 
        currency (:obj:`str`):
            Currency for the product price 
        total_amount (:obj:`int`):
            Product total price in the minimal quantity of the currency
        start_parameter (:obj:`str`):
            Unique invoice bot start_parameterTo share an invoice use the URL https://tme/{bot_username}?start={start_parameter} 
        is_test (:obj:`bool`):
            True, if the invoice is a test invoice
        need_shipping_address (:obj:`bool`):
            True, if the shipping address should be specified 
        receipt_message_id (:obj:`int`):
            The identifier of the message with the receipt, after the product has been purchased

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageInvoice"

    def __init__(self, title, description, photo, currency, total_amount, start_parameter, is_test, need_shipping_address, receipt_message_id, **kwargs):
        
        self.title = title  # str
        self.description = description  # str
        self.photo = photo  # Photo
        self.currency = currency  # str
        self.total_amount = total_amount  # int
        self.start_parameter = start_parameter  # str
        self.is_test = is_test  # bool
        self.need_shipping_address = need_shipping_address  # bool
        self.receipt_message_id = receipt_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageInvoice":
        title = q.get('title')
        description = q.get('description')
        photo = Object.read(q.get('photo'))
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        start_parameter = q.get('start_parameter')
        is_test = q.get('is_test')
        need_shipping_address = q.get('need_shipping_address')
        receipt_message_id = q.get('receipt_message_id')
        return MessageInvoice(title, description, photo, currency, total_amount, start_parameter, is_test, need_shipping_address, receipt_message_id)
