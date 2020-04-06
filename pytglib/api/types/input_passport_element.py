

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
    def read(q: dict, *args) -> "InputPassportElementPersonalDetails or InputPassportElementPhoneNumber or InputPassportElementPassportRegistration or InputPassportElementDriverLicense or InputPassportElementAddress or InputPassportElementUtilityBill or InputPassportElementEmailAddress or InputPassportElementIdentityCard or InputPassportElementPassport or InputPassportElementBankStatement or InputPassportElementTemporaryRegistration or InputPassportElementRentalAgreement or InputPassportElementInternalPassport":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElement()
