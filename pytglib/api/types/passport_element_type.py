

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
    def read(q: dict, *args) -> "PassportElementTypeEmailAddress or PassportElementTypeRentalAgreement or PassportElementTypePersonalDetails or PassportElementTypeAddress or PassportElementTypeBankStatement or PassportElementTypePassportRegistration or PassportElementTypeDriverLicense or PassportElementTypeUtilityBill or PassportElementTypePhoneNumber or PassportElementTypeInternalPassport or PassportElementTypePassport or PassportElementTypeTemporaryRegistration or PassportElementTypeIdentityCard":
        if q.get("@type"):
            return Object.read(q)
        return PassportElementType()
