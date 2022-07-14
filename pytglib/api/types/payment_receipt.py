

from ..utils import Object


class PaymentReceipt(Object):
    """
    Contains information about a successful payment

    Attributes:
        ID (:obj:`str`): ``PaymentReceipt``

    Args:
        title (:obj:`str`):
            Product title
        description (:class:`telegram.api.types.formattedText`):
            Product description
        photo (:class:`telegram.api.types.photo`):
            Product photo; may be null
        date (:obj:`int`):
            Point in time (Unix timestamp) when the payment was made
        seller_bot_user_id (:obj:`int`):
            User identifier of the seller bot
        payment_provider_user_id (:obj:`int`):
            User identifier of the payment provider bot
        invoice (:class:`telegram.api.types.invoice`):
            Information about the invoice
        order_info (:class:`telegram.api.types.orderInfo`):
            Order information; may be null
        shipping_option (:class:`telegram.api.types.shippingOption`):
            Chosen shipping option; may be null
        credentials_title (:obj:`str`):
            Title of the saved credentials chosen by the buyer
        tip_amount (:obj:`int`):
            The amount of tip chosen by the buyer in the smallest units of the currency

    Returns:
        PaymentReceipt

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentReceipt"

    def __init__(self, title, description, photo, date, seller_bot_user_id, payment_provider_user_id, invoice, order_info, shipping_option, credentials_title, tip_amount, **kwargs):
        
        self.title = title  # str
        self.description = description  # FormattedText
        self.photo = photo  # Photo
        self.date = date  # int
        self.seller_bot_user_id = seller_bot_user_id  # int
        self.payment_provider_user_id = payment_provider_user_id  # int
        self.invoice = invoice  # Invoice
        self.order_info = order_info  # OrderInfo
        self.shipping_option = shipping_option  # ShippingOption
        self.credentials_title = credentials_title  # str
        self.tip_amount = tip_amount  # int

    @staticmethod
    def read(q: dict, *args) -> "PaymentReceipt":
        title = q.get('title')
        description = Object.read(q.get('description'))
        photo = Object.read(q.get('photo'))
        date = q.get('date')
        seller_bot_user_id = q.get('seller_bot_user_id')
        payment_provider_user_id = q.get('payment_provider_user_id')
        invoice = Object.read(q.get('invoice'))
        order_info = Object.read(q.get('order_info'))
        shipping_option = Object.read(q.get('shipping_option'))
        credentials_title = q.get('credentials_title')
        tip_amount = q.get('tip_amount')
        return PaymentReceipt(title, description, photo, date, seller_bot_user_id, payment_provider_user_id, invoice, order_info, shipping_option, credentials_title, tip_amount)
