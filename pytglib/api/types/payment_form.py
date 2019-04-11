

from ..utils import Object


class PaymentForm(Object):
    """
    Contains information about an invoice payment form 

    Attributes:
        ID (:obj:`str`): ``PaymentForm``

    Args:
        invoice (:class:`telegram.api.types.invoice`):
            Full information of the invoice 
        url (:obj:`str`):
            Payment form URL 
        payments_provider (:class:`telegram.api.types.paymentsProviderStripe`):
            Contains information about the payment provider, if available, to support it natively without the need for opening the URL; may be null
        saved_order_info (:class:`telegram.api.types.orderInfo`):
            Saved server-side order information; may be null 
        saved_credentials (:class:`telegram.api.types.savedCredentials`):
            Contains information about saved card credentials; may be null 
        can_save_credentials (:obj:`bool`):
            True, if the user can choose to save credentials 
        need_password (:obj:`bool`):
            True, if the user will be able to save credentials protected by a password they set up

    Returns:
        PaymentForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentForm"

    def __init__(self, invoice, url, payments_provider, saved_order_info, saved_credentials, can_save_credentials, need_password, **kwargs):
        
        self.invoice = invoice  # Invoice
        self.url = url  # str
        self.payments_provider = payments_provider  # PaymentsProviderStripe
        self.saved_order_info = saved_order_info  # OrderInfo
        self.saved_credentials = saved_credentials  # SavedCredentials
        self.can_save_credentials = can_save_credentials  # bool
        self.need_password = need_password  # bool

    @staticmethod
    def read(q: dict, *args) -> "PaymentForm":
        invoice = Object.read(q.get('invoice'))
        url = q.get('url')
        payments_provider = Object.read(q.get('payments_provider'))
        saved_order_info = Object.read(q.get('saved_order_info'))
        saved_credentials = Object.read(q.get('saved_credentials'))
        can_save_credentials = q.get('can_save_credentials')
        need_password = q.get('need_password')
        return PaymentForm(invoice, url, payments_provider, saved_order_info, saved_credentials, can_save_credentials, need_password)
