

from ..utils import Object


class InputInvoiceName(Object):
    """
    An invoice from a link of the type internalLinkTypeInvoice 

    Attributes:
        ID (:obj:`str`): ``InputInvoiceName``

    Args:
        name (:obj:`str`):
            Name of the invoice

    Returns:
        InputInvoice

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputInvoiceName"

    def __init__(self, name, **kwargs):
        
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "InputInvoiceName":
        name = q.get('name')
        return InputInvoiceName(name)
