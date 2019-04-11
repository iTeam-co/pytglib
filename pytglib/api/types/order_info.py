

from ..utils import Object


class OrderInfo(Object):
    """
    Order information 

    Attributes:
        ID (:obj:`str`): ``OrderInfo``

    Args:
        name (:obj:`str`):
            Name of the user 
        phone_number (:obj:`str`):
            Phone number of the user 
        email_address (:obj:`str`):
            Email address of the user 
        shipping_address (:class:`telegram.api.types.address`):
            Shipping address for this order; may be null

    Returns:
        OrderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "orderInfo"

    def __init__(self, name, phone_number, email_address, shipping_address, **kwargs):
        
        self.name = name  # str
        self.phone_number = phone_number  # str
        self.email_address = email_address  # str
        self.shipping_address = shipping_address  # Address

    @staticmethod
    def read(q: dict, *args) -> "OrderInfo":
        name = q.get('name')
        phone_number = q.get('phone_number')
        email_address = q.get('email_address')
        shipping_address = Object.read(q.get('shipping_address'))
        return OrderInfo(name, phone_number, email_address, shipping_address)
