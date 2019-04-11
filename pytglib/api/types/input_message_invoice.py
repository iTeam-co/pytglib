

from ..utils import Object


class InputMessageInvoice(Object):
    """
    A message with an invoice; can be used only by bots and only in private chats 

    Attributes:
        ID (:obj:`str`): ``InputMessageInvoice``

    Args:
        invoice (:class:`telegram.api.types.invoice`):
            Invoice 
        title (:obj:`str`):
            Product title; 1-32 characters 
        description (:obj:`str`):
            Product description; 0-255 characters 
        photo_url (:obj:`str`):
            Product photo URL; optional 
        photo_size (:obj:`int`):
            Product photo size 
        photo_width (:obj:`int`):
            Product photo width 
        photo_height (:obj:`int`):
            Product photo height
        payload (:obj:`bytes`):
            The invoice payload 
        provider_token (:obj:`str`):
            Payment provider token 
        provider_data (:obj:`str`):
            JSON-encoded data about the invoice, which will be shared with the payment provider 
        start_parameter (:obj:`str`):
            Unique invoice bot start_parameter for the generation of this invoice

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageInvoice"

    def __init__(self, invoice, title, description, photo_url, photo_size, photo_width, photo_height, payload, provider_token, provider_data, start_parameter, **kwargs):
        
        self.invoice = invoice  # Invoice
        self.title = title  # str
        self.description = description  # str
        self.photo_url = photo_url  # str
        self.photo_size = photo_size  # int
        self.photo_width = photo_width  # int
        self.photo_height = photo_height  # int
        self.payload = payload  # bytes
        self.provider_token = provider_token  # str
        self.provider_data = provider_data  # str
        self.start_parameter = start_parameter  # str

    @staticmethod
    def read(q: dict, *args) -> "InputMessageInvoice":
        invoice = Object.read(q.get('invoice'))
        title = q.get('title')
        description = q.get('description')
        photo_url = q.get('photo_url')
        photo_size = q.get('photo_size')
        photo_width = q.get('photo_width')
        photo_height = q.get('photo_height')
        payload = q.get('payload')
        provider_token = q.get('provider_token')
        provider_data = q.get('provider_data')
        start_parameter = q.get('start_parameter')
        return InputMessageInvoice(invoice, title, description, photo_url, photo_size, photo_width, photo_height, payload, provider_token, provider_data, start_parameter)
