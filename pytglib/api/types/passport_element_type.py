

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
    def read(q: dict, *args) -> "PassportElementTypeRentalAgreement or PassportElementTypeDriverLicense or PassportElementTypeTemporaryRegistration or PassportElementTypePassportRegistration or PassportElementTypePersonalDetails or PassportElementTypeIdentityCard or PassportElementTypeInternalPassport or PassportElementTypeUtilityBill or PassportElementTypeAddress or PassportElementTypePhoneNumber or PassportElementTypeEmailAddress or PassportElementTypeBankStatement or PassportElementTypePassport":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementType()
