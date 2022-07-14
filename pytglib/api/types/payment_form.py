

from ..utils import Object


class PaymentForm(Object):
    """
    Contains information about an invoice payment form

    Attributes:
        ID (:obj:`str`): ``PaymentForm``

    Args:
        id (:obj:`int`):
            The payment form identifier
        invoice (:class:`telegram.api.types.invoice`):
            Full information about the invoice
        seller_bot_user_id (:obj:`int`):
            User identifier of the seller bot
        payment_provider_user_id (:obj:`int`):
            User identifier of the payment provider bot
        payment_provider (:class:`telegram.api.types.PaymentProvider`):
            Information about the payment provider
        saved_order_info (:class:`telegram.api.types.orderInfo`):
            Saved server-side order information; may be null
        saved_credentials (:class:`telegram.api.types.savedCredentials`):
            Information about saved card credentials; may be null
        can_save_credentials (:obj:`bool`):
            True, if the user can choose to save credentials
        need_password (:obj:`bool`):
            True, if the user will be able to save credentials protected by a password they set up
        product_title (:obj:`str`):
            Product title
        product_description (:class:`telegram.api.types.formattedText`):
            Product description
        product_photo (:class:`telegram.api.types.photo`):
            Product photo; may be null

    Returns:
        PaymentForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentForm"

    def __init__(self, id, invoice, seller_bot_user_id, payment_provider_user_id, payment_provider, saved_order_info, saved_credentials, can_save_credentials, need_password, product_title, product_description, product_photo, **kwargs):
        
        self.id = id  # int
        self.invoice = invoice  # Invoice
        self.seller_bot_user_id = seller_bot_user_id  # int
        self.payment_provider_user_id = payment_provider_user_id  # int
        self.payment_provider = payment_provider  # PaymentProvider
        self.saved_order_info = saved_order_info  # OrderInfo
        self.saved_credentials = saved_credentials  # SavedCredentials
        self.can_save_credentials = can_save_credentials  # bool
        self.need_password = need_password  # bool
        self.product_title = product_title  # str
        self.product_description = product_description  # FormattedText
        self.product_photo = product_photo  # Photo

    @staticmethod
    def read(q: dict, *args) -> "PaymentForm":
        id = q.get('id')
        invoice = Object.read(q.get('invoice'))
        seller_bot_user_id = q.get('seller_bot_user_id')
        payment_provider_user_id = q.get('payment_provider_user_id')
        payment_provider = Object.read(q.get('payment_provider'))
        saved_order_info = Object.read(q.get('saved_order_info'))
        saved_credentials = Object.read(q.get('saved_credentials'))
        can_save_credentials = q.get('can_save_credentials')
        need_password = q.get('need_password')
        product_title = q.get('product_title')
        product_description = Object.read(q.get('product_description'))
        product_photo = Object.read(q.get('product_photo'))
        return PaymentForm(id, invoice, seller_bot_user_id, payment_provider_user_id, payment_provider, saved_order_info, saved_credentials, can_save_credentials, need_password, product_title, product_description, product_photo)
