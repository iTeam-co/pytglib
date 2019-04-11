

from ..utils import Object


class SendPaymentForm(Object):
    """
    Sends a filled-out payment form to the bot for final verification 

    Attributes:
        ID (:obj:`str`): ``SendPaymentForm``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the Invoice message 
        message_id (:obj:`int`):
            Message identifier 
        order_info_id (:obj:`str`):
            Identifier returned by ValidateOrderInfo, or an empty string 
        shipping_option_id (:obj:`str`):
            Identifier of a chosen shipping option, if applicable
        credentials (:class:`telegram.api.types.InputCredentials`):
            The credentials chosen by user for payment

    Returns:
        PaymentResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPaymentForm"

    def __init__(self, chat_id, message_id, order_info_id, shipping_option_id, credentials, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.order_info_id = order_info_id  # str
        self.shipping_option_id = shipping_option_id  # str
        self.credentials = credentials  # InputCredentials

    @staticmethod
    def read(q: dict, *args) -> "SendPaymentForm":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        order_info_id = q.get('order_info_id')
        shipping_option_id = q.get('shipping_option_id')
        credentials = Object.read(q.get('credentials'))
        return SendPaymentForm(chat_id, message_id, order_info_id, shipping_option_id, credentials)
