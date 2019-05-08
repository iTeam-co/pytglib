

from ..utils import Object


class PushMessageContentInvoice(Object):
    """
    A message with an invoice from a bot 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentInvoice``

    Args:
        price (:obj:`str`):
            Product price 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentInvoice"

    def __init__(self, price, is_pinned, **kwargs):
        
        self.price = price  # str
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentInvoice":
        price = q.get('price')
        is_pinned = q.get('is_pinned')
        return PushMessageContentInvoice(price, is_pinned)
