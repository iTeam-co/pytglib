

from ..utils import Object


class PaymentResult(Object):
    """
    Contains the result of a payment request 

    Attributes:
        ID (:obj:`str`): ``PaymentResult``

    Args:
        success (:obj:`bool`):
            True, if the payment request was successful; otherwise the verification_url will be not empty 
        verification_url (:obj:`str`):
            URL for additional payment credentials verification

    Returns:
        PaymentResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "paymentResult"

    def __init__(self, success, verification_url, **kwargs):
        
        self.success = success  # bool
        self.verification_url = verification_url  # str

    @staticmethod
    def read(q: dict, *args) -> "PaymentResult":
        success = q.get('success')
        verification_url = q.get('verification_url')
        return PaymentResult(success, verification_url)
