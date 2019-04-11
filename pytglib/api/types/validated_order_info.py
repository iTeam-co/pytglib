

from ..utils import Object


class ValidatedOrderInfo(Object):
    """
    Contains a temporary identifier of validated order information, which is stored for one hour. Also contains the available shipping options 

    Attributes:
        ID (:obj:`str`): ``ValidatedOrderInfo``

    Args:
        order_info_id (:obj:`str`):
            Temporary identifier of the order information 
        shipping_options (List of :class:`telegram.api.types.shippingOption`):
            Available shipping options

    Returns:
        ValidatedOrderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "validatedOrderInfo"

    def __init__(self, order_info_id, shipping_options, **kwargs):
        
        self.order_info_id = order_info_id  # str
        self.shipping_options = shipping_options  # list of shippingOption

    @staticmethod
    def read(q: dict, *args) -> "ValidatedOrderInfo":
        order_info_id = q.get('order_info_id')
        shipping_options = [Object.read(i) for i in q.get('shipping_options', [])]
        return ValidatedOrderInfo(order_info_id, shipping_options)
