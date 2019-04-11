

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
    def read(q: dict, *args) -> "PassportElementDriverLicense or PassportElementUtilityBill or PassportElementEmailAddress or PassportElementTemporaryRegistration or PassportElementIdentityCard or PassportElementInternalPassport or PassportElementRentalAgreement or PassportElementPassport or PassportElementBankStatement or PassportElementAddress or PassportElementPersonalDetails or PassportElementPassportRegistration or PassportElementPhoneNumber":
        if q.get("@type"):
            return Object.read(q)
        return PassportElement()
