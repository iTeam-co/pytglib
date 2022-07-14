

from ..utils import Object


class InternalLinkTypeInvoice(Object):
    """
    The link is a link to an invoice. Call getPaymentForm with the given invoice name to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeInvoice``

    Args:
        invoice_name (:obj:`str`):
            Name of the invoice

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeInvoice"

    def __init__(self, invoice_name, **kwargs):
        
        self.invoice_name = invoice_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeInvoice":
        invoice_name = q.get('invoice_name')
        return InternalLinkTypeInvoice(invoice_name)
