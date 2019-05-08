

from ..utils import Object


class PassportElement(Object):
    """
    Contains information about a Telegram Passport element

    No parameters required.
    """
    ID = "passportElement"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementAddress or PassportElementRentalAgreement or PassportElementEmailAddress or PassportElementPassport or PassportElementPhoneNumber or PassportElementBankStatement or PassportElementUtilityBill or PassportElementPassportRegistration or PassportElementPersonalDetails or PassportElementTemporaryRegistration or PassportElementDriverLicense or PassportElementIdentityCard or PassportElementInternalPassport":
        if q.get("@type"):
            return Object.read(q)
        return PassportElement()
