

from ..utils import Object


class PaymentProviderSmartGlocal(Object):
    """
    Smart Glocal payment provider 

    Attributes:
        ID (:obj:`str`): ``PaymentProviderSmartGlocal``

    Args:
        public_token (:obj:`str`):
            Public payment token

    Returns:
        PaymentProvider

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentProviderSmartGlocal"

    def __init__(self, public_token, **kwargs):
        
        self.public_token = public_token  # str

    @staticmethod
    def read(q: dict, *args) -> "PaymentProviderSmartGlocal":
        public_token = q.get('public_token')
        return PaymentProviderSmartGlocal(public_token)
