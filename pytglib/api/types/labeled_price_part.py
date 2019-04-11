

from ..utils import Object


class LabeledPricePart(Object):
    """
    Portion of the price of a product (e.g., "delivery cost", "tax amount") 

    Attributes:
        ID (:obj:`str`): ``LabeledPricePart``

    Args:
        label (:obj:`str`):
            Label for this portion of the product price 
        amount (:obj:`int`):
            Currency amount in minimal quantity of the currency

    Returns:
        LabeledPricePart

    Raises:
        :class:`telegram.Error`
    """
    ID = "labeledPricePart"

    def __init__(self, label, amount, **kwargs):
        
        self.label = label  # str
        self.amount = amount  # int

    @staticmethod
    def read(q: dict, *args) -> "LabeledPricePart":
        label = q.get('label')
        amount = q.get('amount')
        return LabeledPricePart(label, amount)
