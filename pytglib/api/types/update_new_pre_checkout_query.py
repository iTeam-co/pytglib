

from ..utils import Object


class UpdateNewPreCheckoutQuery(Object):
    """
    A new incoming pre-checkout query; for bots only. Contains full information about a checkout 

    Attributes:
        ID (:obj:`str`): ``UpdateNewPreCheckoutQuery``

    Args:
        id (:obj:`int`):
            Unique query identifier 
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query 
        currency (:obj:`str`):
            Currency for the product price 
        total_amount (:obj:`int`):
            Total price for the product, in the minimal quantity of the currency
        invoice_payload (:obj:`bytes`):
            Invoice payload 
        shipping_option_id (:obj:`str`):
            Identifier of a shipping option chosen by the user; may be empty if not applicable 
        order_info (:class:`telegram.api.types.orderInfo`):
            Information about the order; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewPreCheckoutQuery"

    def __init__(self, id, sender_user_id, currency, total_amount, invoice_payload, shipping_option_id, order_info, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.currency = currency  # str
        self.total_amount = total_amount  # int
        self.invoice_payload = invoice_payload  # bytes
        self.shipping_option_id = shipping_option_id  # str
        self.order_info = order_info  # OrderInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewPreCheckoutQuery":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        invoice_payload = q.get('invoice_payload')
        shipping_option_id = q.get('shipping_option_id')
        order_info = Object.read(q.get('order_info'))
        return UpdateNewPreCheckoutQuery(id, sender_user_id, currency, total_amount, invoice_payload, shipping_option_id, order_info)
