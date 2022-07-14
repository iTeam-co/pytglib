

from ..utils import Object


class ValidateOrderInfo(Object):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice

    Attributes:
        ID (:obj:`str`): ``ValidateOrderInfo``

    Args:
        input_invoice (:class:`telegram.api.types.InputInvoice`):
            The invoice
        order_info (:class:`telegram.api.types.orderInfo`):
            The order information, provided by the user; pass null if empty
        allow_save (:obj:`bool`):
            Pass true to save the order information

    Returns:
        ValidatedOrderInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "validateOrderInfo"

    def __init__(self, input_invoice, order_info, allow_save, extra=None, **kwargs):
        self.extra = extra
        self.input_invoice = input_invoice  # InputInvoice
        self.order_info = order_info  # OrderInfo
        self.allow_save = allow_save  # bool

    @staticmethod
    def read(q: dict, *args) -> "ValidateOrderInfo":
        input_invoice = Object.read(q.get('input_invoice'))
        order_info = Object.read(q.get('order_info'))
        allow_save = q.get('allow_save')
        return ValidateOrderInfo(input_invoice, order_info, allow_save)
