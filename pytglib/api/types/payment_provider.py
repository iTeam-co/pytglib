

from ..utils import Object


class PaymentProvider(Object):
    """
    Contains information about a payment provider

    No parameters required.
    """
    ID = "paymentProvider"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PaymentProviderStripe or PaymentProviderOther or PaymentProviderSmartGlocal":
        if q.get("@type"):
            return Object.read(q)
        return PaymentProvider()
