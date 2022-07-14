

from ..utils import Object


class GetPaymentForm(Object):
    """
    Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy

    Attributes:
        ID (:obj:`str`): ``GetPaymentForm``

    Args:
        input_invoice (:class:`telegram.api.types.InputInvoice`):
            The invoice
        theme (:class:`telegram.api.types.themeParameters`):
            Preferred payment form theme; pass null to use the default theme

    Returns:
        PaymentForm

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPaymentForm"

    def __init__(self, input_invoice, theme, extra=None, **kwargs):
        self.extra = extra
        self.input_invoice = input_invoice  # InputInvoice
        self.theme = theme  # ThemeParameters

    @staticmethod
    def read(q: dict, *args) -> "GetPaymentForm":
        input_invoice = Object.read(q.get('input_invoice'))
        theme = Object.read(q.get('theme'))
        return GetPaymentForm(input_invoice, theme)
