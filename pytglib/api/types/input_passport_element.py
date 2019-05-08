

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
    def read(q: dict, *args) -> "InputPassportElementDriverLicense or InputPassportElementPersonalDetails or InputPassportElementIdentityCard or InputPassportElementPassport or InputPassportElementPassportRegistration or InputPassportElementRentalAgreement or InputPassportElementInternalPassport or InputPassportElementTemporaryRegistration or InputPassportElementEmailAddress or InputPassportElementBankStatement or InputPassportElementPhoneNumber or InputPassportElementAddress or InputPassportElementUtilityBill":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElement()
