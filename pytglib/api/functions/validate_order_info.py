

from ..utils import Object


class ValidateOrderInfo(Object):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice 

    Attributes:
        ID (:obj:`str`): ``ValidateOrderInfo``

    Args:
        chat_id (:obj:`int`):
            Chat identifier of the Invoice message 
        message_id (:obj:`int`):
            Message identifier 
        order_info (:class:`telegram.api.types.orderInfo`):
            The order information, provided by the user 
        allow_save (:obj:`bool`):
            True, if the order information can be saved

    Returns:
        ValidatedOrderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "validateOrderInfo"

    def __init__(self, chat_id, message_id, order_info, allow_save, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.order_info = order_info  # OrderInfo
        self.allow_save = allow_save  # bool

    @staticmethod
    def read(q: dict, *args) -> "ValidateOrderInfo":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        order_info = Object.read(q.get('order_info'))
        allow_save = q.get('allow_save')
        return ValidateOrderInfo(chat_id, message_id, order_info, allow_save)
