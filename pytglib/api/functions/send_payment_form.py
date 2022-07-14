

from ..utils import Object


class SendPaymentForm(Object):
    """
    Sends a filled-out payment form to the bot for final verification 

    Attributes:
        ID (:obj:`str`): ``SendPaymentForm``

    Args:
        input_invoice (:class:`telegram.api.types.InputInvoice`):
            The invoice
        payment_form_id (:obj:`int`):
            Payment form identifier returned by getPaymentForm 
        order_info_id (:obj:`str`):
            Identifier returned by validateOrderInfo, or an empty string 
        shipping_option_id (:obj:`str`):
            Identifier of a chosen shipping option, if applicable
        credentials (:class:`telegram.api.types.InputCredentials`):
            The credentials chosen by user for payment 
        tip_amount (:obj:`int`):
            Chosen by the user amount of tip in the smallest units of the currency

    Returns:
        PaymentResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPaymentForm"

    def __init__(self, input_invoice, payment_form_id, order_info_id, shipping_option_id, credentials, tip_amount, extra=None, **kwargs):
        self.extra = extra
        self.input_invoice = input_invoice  # InputInvoice
        self.payment_form_id = payment_form_id  # int
        self.order_info_id = order_info_id  # str
        self.shipping_option_id = shipping_option_id  # str
        self.credentials = credentials  # InputCredentials
        self.tip_amount = tip_amount  # int

    @staticmethod
    def read(q: dict, *args) -> "SendPaymentForm":
        input_invoice = Object.read(q.get('input_invoice'))
        payment_form_id = q.get('payment_form_id')
        order_info_id = q.get('order_info_id')
        shipping_option_id = q.get('shipping_option_id')
        credentials = Object.read(q.get('credentials'))
        tip_amount = q.get('tip_amount')
        return SendPaymentForm(input_invoice, payment_form_id, order_info_id, shipping_option_id, credentials, tip_amount)
