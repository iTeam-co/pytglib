

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
    def read(q: dict, *args) -> "PassportElementTypeBankStatement or PassportElementTypeUtilityBill or PassportElementTypeIdentityCard or PassportElementTypeTemporaryRegistration or PassportElementTypeEmailAddress or PassportElementTypePhoneNumber or PassportElementTypePassportRegistration or PassportElementTypePersonalDetails or PassportElementTypeAddress or PassportElementTypeInternalPassport or PassportElementTypeRentalAgreement or PassportElementTypeDriverLicense or PassportElementTypePassport":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementType()
