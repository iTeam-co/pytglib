

from ..utils import Object


class GetPaymentForm(Object):
    """
    Returns an invoice payment form. This method should be called when the user presses inlineKeyboardButtonBuy 

    Attributes:
        ID (:obj:`str`): ``GetPaymentForm``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the Invoice message 
        message_id (:obj:`int`):
            Message identifier

    Returns:
        PaymentForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPaymentForm"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetPaymentForm":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetPaymentForm(chat_id, message_id)
