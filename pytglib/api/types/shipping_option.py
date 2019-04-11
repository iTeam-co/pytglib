

from ..utils import Object


class ShippingOption(Object):
    """
    One shipping option 

    Attributes:
        ID (:obj:`str`): ``ShippingOption``

    Args:
        id (:obj:`str`):
            Shipping option identifier 
        title (:obj:`str`):
            Option title 
        price_parts (List of :class:`telegram.api.types.labeledPricePart`):
            A list of objects used to calculate the total shipping costs

    Returns:
        ShippingOption

    Raises:
        :class:`telegram.Error`
    """
    ID = "shippingOption"

    def __init__(self, id, title, price_parts, **kwargs):
        
        self.id = id  # str
        self.title = title  # str
        self.price_parts = price_parts  # list of labeledPricePart

    @staticmethod
    def read(q: dict, *args) -> "ShippingOption":
        id = q.get('id')
        title = q.get('title')
        price_parts = [Object.read(i) for i in q.get('price_parts', [])]
        return ShippingOption(id, title, price_parts)
