

from ..utils import Object


class MessagePaymentSuccessful(Object):
    """
    A payment has been completed 

    Attributes:
        ID (:obj:`str`): ``MessagePaymentSuccessful``

    Args:
        invoice_message_id (:obj:`int`):
            Identifier of the message with the corresponding invoice; can be an identifier of a deleted message 
        currency (:obj:`str`):
            Currency for the price of the product 
        total_amount (:obj:`int`):
            Total price for the product, in the minimal quantity of the currency

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePaymentSuccessful"

    def __init__(self, invoice_message_id, currency, total_amount, **kwargs):
        
        self.invoice_message_id = invoice_message_id  # int
        self.currency = currency  # str
        self.total_amount = total_amount  # int

    @staticmethod
    def read(q: dict, *args) -> "MessagePaymentSuccessful":
        invoice_message_id = q.get('invoice_message_id')
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        return MessagePaymentSuccessful(invoice_message_id, currency, total_amount)
