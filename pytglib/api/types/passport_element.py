

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
    def read(q: dict, *args) -> "PassportElementUtilityBill or PassportElementRentalAgreement or PassportElementAddress or PassportElementBankStatement or PassportElementTemporaryRegistration or PassportElementPersonalDetails or PassportElementPassport or PassportElementDriverLicense or PassportElementEmailAddress or PassportElementIdentityCard or PassportElementPassportRegistration or PassportElementPhoneNumber or PassportElementInternalPassport":
        if q.get("@type"):
            return Object.read(q)
        return PassportElement()
