

from ..utils import Object


class MessagePaymentSuccessfulBot(Object):
    """
    A payment has been completed; for bots only 

    Attributes:
        ID (:obj:`str`): ``MessagePaymentSuccessfulBot``

    Args:
        currency (:obj:`str`):
            Currency for price of the product 
        total_amount (:obj:`int`):
            Total price for the product, in the smallest units of the currency
        is_recurring (:obj:`bool`):
            True, if this is a recurring payment 
        is_first_recurring (:obj:`bool`):
            True, if this is the first recurring payment
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

    def __init__(self, currency, total_amount, is_recurring, is_first_recurring, invoice_payload, shipping_option_id, order_info, telegram_payment_charge_id, provider_payment_charge_id, **kwargs):
        
        self.currency = currency  # str
        self.total_amount = total_amount  # int
        self.is_recurring = is_recurring  # bool
        self.is_first_recurring = is_first_recurring  # bool
        self.invoice_payload = invoice_payload  # bytes
        self.shipping_option_id = shipping_option_id  # str
        self.order_info = order_info  # OrderInfo
        self.telegram_payment_charge_id = telegram_payment_charge_id  # str
        self.provider_payment_charge_id = provider_payment_charge_id  # str

    @staticmethod
    def read(q: dict, *args) -> "MessagePaymentSuccessfulBot":
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        is_recurring = q.get('is_recurring')
        is_first_recurring = q.get('is_first_recurring')
        invoice_payload = q.get('invoice_payload')
        shipping_option_id = q.get('shipping_option_id')
        order_info = Object.read(q.get('order_info'))
        telegram_payment_charge_id = q.get('telegram_payment_charge_id')
        provider_payment_charge_id = q.get('provider_payment_charge_id')
        return MessagePaymentSuccessfulBot(currency, total_amount, is_recurring, is_first_recurring, invoice_payload, shipping_option_id, order_info, telegram_payment_charge_id, provider_payment_charge_id)
