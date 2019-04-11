

from ..utils import Object


class MessagePaymentSuccessfulBot(Object):
    """
    A payment has been completed; for bots only 

    Attributes:
        ID (:obj:`str`): ``MessagePaymentSuccessfulBot``

    Args:
        invoice_message_id (:obj:`int`):
            Identifier of the message with the corresponding invoice; can be an identifier of a deleted message 
        currency (:obj:`str`):
            Currency for price of the product
        total_amount (:obj:`int`):
            Total price for the product, in the minimal quantity of the currency 
        invoice_payload (:obj:`bytes`):
            Invoice payload 
        shipping_option_id (:obj:`str`):
            Identifier of the shipping option chosen by the user; may be empty if not applicable 
        order_info (:class:`telegram.api.types.orderInfo`):
            Information about the order; may be null
        telegram_payment_charge_id (:obj:`str`):
            Telegram payment identifier 
        provider_payment_charge_id (:obj:`str`):
            Provider payment identifier

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePaymentSuccessfulBot"

    def __init__(self, invoice_message_id, currency, total_amount, invoice_payload, shipping_option_id, order_info, telegram_payment_charge_id, provider_payment_charge_id, **kwargs):
        
        self.invoice_message_id = invoice_message_id  # int
        self.currency = currency  # str
        self.total_amount = total_amount  # int
        self.invoice_payload = invoice_payload  # bytes
        self.shipping_option_id = shipping_option_id  # str
        self.order_info = order_info  # OrderInfo
        self.telegram_payment_charge_id = telegram_payment_charge_id  # str
        self.provider_payment_charge_id = provider_payment_charge_id  # str

    @staticmethod
    def read(q: dict, *args) -> "MessagePaymentSuccessfulBot":
        invoice_message_id = q.get('invoice_message_id')
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        invoice_payload = q.get('invoice_payload')
        shipping_option_id = q.get('shipping_option_id')
        order_info = Object.read(q.get('order_info'))
        telegram_payment_charge_id = q.get('telegram_payment_charge_id')
        provider_payment_charge_id = q.get('provider_payment_charge_id')
        return MessagePaymentSuccessfulBot(invoice_message_id, currency, total_amount, invoice_payload, shipping_option_id, order_info, telegram_payment_charge_id, provider_payment_charge_id)
