

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
    def read(q: dict, *args) -> "InputPassportElementEmailAddress or InputPassportElementPassport or InputPassportElementUtilityBill or InputPassportElementIdentityCard or InputPassportElementDriverLicense or InputPassportElementBankStatement or InputPassportElementPersonalDetails or InputPassportElementPhoneNumber or InputPassportElementPassportRegistration or InputPassportElementTemporaryRegistration or InputPassportElementAddress or InputPassportElementRentalAgreement or InputPassportElementInternalPassport":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElement()
