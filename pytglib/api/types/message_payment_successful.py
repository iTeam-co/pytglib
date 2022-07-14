

from ..utils import Object


class MessagePaymentSuccessful(Object):
    """
    A payment has been completed 

    Attributes:
        ID (:obj:`str`): ``MessagePaymentSuccessful``

    Args:
        invoice_chat_id (:obj:`int`):
            Identifier of the chat, containing the corresponding invoice message; 0 if unknown 
        invoice_message_id (:obj:`int`):
            Identifier of the message with the corresponding invoice; can be 0 or an identifier of a deleted message
        currency (:obj:`str`):
            Currency for the price of the product 
        total_amount (:obj:`int`):
            Total price for the product, in the smallest units of the currency
        is_recurring (:obj:`bool`):
            True, if this is a recurring payment 
        is_first_recurring (:obj:`bool`):
            True, if this is the first recurring payment 
        invoice_name (:obj:`str`):
            Name of the invoice; may be empty if unknown

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePaymentSuccessful"

    def __init__(self, invoice_chat_id, invoice_message_id, currency, total_amount, is_recurring, is_first_recurring, invoice_name, **kwargs):
        
        self.invoice_chat_id = invoice_chat_id  # int
        self.invoice_message_id = invoice_message_id  # int
        self.currency = currency  # str
        self.total_amount = total_amount  # int
        self.is_recurring = is_recurring  # bool
        self.is_first_recurring = is_first_recurring  # bool
        self.invoice_name = invoice_name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessagePaymentSuccessful":
        invoice_chat_id = q.get('invoice_chat_id')
        invoice_message_id = q.get('invoice_message_id')
        currency = q.get('currency')
        total_amount = q.get('total_amount')
        is_recurring = q.get('is_recurring')
        is_first_recurring = q.get('is_first_recurring')
        invoice_name = q.get('invoice_name')
        return MessagePaymentSuccessful(invoice_chat_id, invoice_message_id, currency, total_amount, is_recurring, is_first_recurring, invoice_name)
