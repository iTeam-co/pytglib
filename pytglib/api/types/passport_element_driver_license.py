

from ..utils import Object


class PassportElementDriverLicense(Object):
    """
    A Telegram Passport element containing the user's driver license 

    Attributes:
        ID (:obj:`str`): ``PassportElementDriverLicense``

    Args:
        driver_license (:class:`telegram.api.types.identityDocument`):
            Driver license

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementDriverLicense"

    def __init__(self, driver_license, **kwargs):
        
        self.driver_license = driver_license  # IdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "PassportElementDriverLicense":
        driver_license = Object.read(q.get('driver_license'))
        return PassportElementDriverLicense(driver_license)
