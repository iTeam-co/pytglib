

from ..utils import Object


class UpdateNewShippingQuery(Object):
    """
    A new incoming shipping query; for bots only. Only for invoices with flexible price 

    Attributes:
        ID (:obj:`str`): ``UpdateNewShippingQuery``

    Args:
        id (:obj:`int`):
            Unique query identifier 
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query 
        invoice_payload (:obj:`str`):
            Invoice payload 
        shipping_address (:class:`telegram.api.types.address`):
            User shipping address

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewShippingQuery"

    def __init__(self, id, sender_user_id, invoice_payload, shipping_address, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.invoice_payload = invoice_payload  # str
        self.shipping_address = shipping_address  # Address

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewShippingQuery":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        invoice_payload = q.get('invoice_payload')
        shipping_address = Object.read(q.get('shipping_address'))
        return UpdateNewShippingQuery(id, sender_user_id, invoice_payload, shipping_address)
