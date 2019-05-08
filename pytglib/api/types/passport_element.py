

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
    def read(q: dict, *args) -> "PassportElementPassport or PassportElementPersonalDetails or PassportElementRentalAgreement or PassportElementPassportRegistration or PassportElementIdentityCard or PassportElementBankStatement or PassportElementUtilityBill or PassportElementTemporaryRegistration or PassportElementDriverLicense or PassportElementEmailAddress or PassportElementInternalPassport or PassportElementPhoneNumber or PassportElementAddress":
        if q.get("@type"):
            return Object.read(q)
        return PassportElement()
