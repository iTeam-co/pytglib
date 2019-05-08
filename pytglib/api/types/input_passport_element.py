

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
    def read(q: dict, *args) -> "InputPassportElementPassport or InputPassportElementPersonalDetails or InputPassportElementPassportRegistration or InputPassportElementUtilityBill or InputPassportElementAddress or InputPassportElementBankStatement or InputPassportElementRentalAgreement or InputPassportElementPhoneNumber or InputPassportElementEmailAddress or InputPassportElementTemporaryRegistration or InputPassportElementIdentityCard or InputPassportElementDriverLicense or InputPassportElementInternalPassport":
        if q.get("@type"):
            return Object.read(q)
        return InputPassportElement()
