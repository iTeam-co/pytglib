

from ..utils import Object


class InputPassportElement(Object):
    """
    Contains information about a Telegram Passport element to be saved

    No parameters required.
    """
    ID = "inputPassportElement"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementTemporaryRegistration or InputPassportElementIdentityCard or InputPassportElementPassportRegistration or InputPassportElementUtilityBill or InputPassportElementPersonalDetails or InputPassportElementDriverLicense or InputPassportElementAddress or InputPassportElementBankStatement or InputPassportElementRentalAgreement or InputPassportElementInternalPassport or InputPassportElementPassport or InputPassportElementPhoneNumber or InputPassportElementEmailAddress":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElement()
