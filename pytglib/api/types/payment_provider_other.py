

from ..utils import Object


class PaymentProviderOther(Object):
    """
    Some other payment provider, for which a web payment form must be shown 

    Attributes:
        ID (:obj:`str`): ``PaymentProviderOther``

    Args:
        url (:obj:`str`):
            Payment form URL

    Returns:
        PaymentProvider

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentProviderOther"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "PaymentProviderOther":
        url = q.get('url')
        return PaymentProviderOther(url)
