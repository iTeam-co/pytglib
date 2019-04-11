

from ..utils import Object


class GetPaymentReceipt(Object):
    """
    Returns information about a successful payment 

    Attributes:
        ID (:obj:`str`): ``GetPaymentReceipt``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the PaymentSuccessful message 
        message_id (:obj:`int`):
            Message identifier

    Returns:
        PaymentReceipt

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPaymentReceipt"

    def __init__(self, chat_id, message_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetPaymentReceipt":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        return GetPaymentReceipt(chat_id, message_id)
