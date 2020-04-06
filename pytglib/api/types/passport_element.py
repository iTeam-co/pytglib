

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
    def read(q: dict, *args) -> "PassportElementIdentityCard or PassportElementPersonalDetails or PassportElementPassport or PassportElementBankStatement or PassportElementPassportRegistration or PassportElementPhoneNumber or PassportElementEmailAddress or PassportElementTemporaryRegistration or PassportElementUtilityBill or PassportElementInternalPassport or PassportElementDriverLicense or PassportElementAddress or PassportElementRentalAgreement":
        if q.get("@type"):
            return Object.read(q)
        return PassportElement()
