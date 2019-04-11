

from ..utils import Object


class PaymentReceipt(Object):
    """
    Contains information about a successful payment 

    Attributes:
        ID (:obj:`str`): ``PaymentReceipt``

    Args:
        date (:obj:`int`):
            Point in time (Unix timestamp) when the payment was made 
        payments_provider_user_id (:obj:`int`):
            User identifier of the payment provider bot 
        invoice (:class:`telegram.api.types.invoice`):
            Contains information about the invoice
        order_info (:class:`telegram.api.types.orderInfo`):
            Contains order information; may be null 
        shipping_option (:class:`telegram.api.types.shippingOption`):
            Chosen shipping option; may be null 
        credentials_title (:obj:`str`):
            Title of the saved credentials

    Returns:
        PaymentReceipt

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentReceipt"

    def __init__(self, date, payments_provider_user_id, invoice, order_info, shipping_option, credentials_title, **kwargs):
        
        self.date = date  # int
        self.payments_provider_user_id = payments_provider_user_id  # int
        self.invoice = invoice  # Invoice
        self.order_info = order_info  # OrderInfo
        self.shipping_option = shipping_option  # ShippingOption
        self.credentials_title = credentials_title  # str

    @staticmethod
    def read(q: dict, *args) -> "PaymentReceipt":
        date = q.get('date')
        payments_provider_user_id = q.get('payments_provider_user_id')
        invoice = Object.read(q.get('invoice'))
        order_info = Object.read(q.get('order_info'))
        shipping_option = Object.read(q.get('shipping_option'))
        credentials_title = q.get('credentials_title')
        return PaymentReceipt(date, payments_provider_user_id, invoice, order_info, shipping_option, credentials_title)
