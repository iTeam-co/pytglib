

from ..utils import Object


class InputCredentials(Object):
    """
    Contains information about the payment method chosen by the user

    No parameters required.
    """
    ID = "inputCredentials"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputCredentialsNew or InputCredentialsSaved or InputCredentialsApplePay or InputCredentialsAndroidPay":
        if q.get("@type"):
            return Object.read(q)
        return InputCredentials()
