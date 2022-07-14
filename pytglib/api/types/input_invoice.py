

from ..utils import Object


class InputInvoice(Object):
    """
    Describe an invoice to process

    No parameters required.
    """
    ID = "inputInvoice"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputInvoiceName or InputInvoiceMessage":
        if q.get("@type"):
            return Object.read(q)
        return InputInvoice()
