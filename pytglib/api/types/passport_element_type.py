

from ..utils import Object


class PassportElementType(Object):
    """
    Contains the type of a Telegram Passport element

    No parameters required.
    """
    ID = "passportElementType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PassportElementTypeUtilityBill or PassportElementTypeRentalAgreement or PassportElementTypeEmailAddress or PassportElementTypePassport or PassportElementTypeDriverLicense or PassportElementTypeAddress or PassportElementTypePassportRegistration or PassportElementTypeTemporaryRegistration or PassportElementTypeInternalPassport or PassportElementTypeBankStatement or PassportElementTypePhoneNumber or PassportElementTypeIdentityCard or PassportElementTypePersonalDetails":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementType()
