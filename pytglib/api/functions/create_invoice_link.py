

from ..utils import Object


class CreateInvoiceLink(Object):
    """
    Creates a link for the given invoice; for bots only 

    Attributes:
        ID (:obj:`str`): ``CreateInvoiceLink``

    Args:
        invoice (:class:`telegram.api.types.InputMessageContent`):
            Information about the invoice of the type inputMessageInvoice

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "createInvoiceLink"

    def __init__(self, invoice, extra=None, **kwargs):
        self.extra = extra
        self.invoice = invoice  # InputMessageContent

    @staticmethod
    def read(q: dict, *args) -> "CreateInvoiceLink":
        invoice = Object.read(q.get('invoice'))
        return CreateInvoiceLink(invoice)
