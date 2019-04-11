

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
    def read(q: dict, *args) -> "PassportElementTypePassport or PassportElementTypeIdentityCard or PassportElementTypeRentalAgreement or PassportElementTypeEmailAddress or PassportElementTypePhoneNumber or PassportElementTypeDriverLicense or PassportElementTypeAddress or PassportElementTypeTemporaryRegistration or PassportElementTypeBankStatement or PassportElementTypeInternalPassport or PassportElementTypeUtilityBill or PassportElementTypePassportRegistration or PassportElementTypePersonalDetails":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementType()
