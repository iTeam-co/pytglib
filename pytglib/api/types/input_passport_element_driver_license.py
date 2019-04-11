

from ..utils import Object


class InputPassportElementDriverLicense(Object):
    """
    A Telegram Passport element to be saved containing the user's driver license 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementDriverLicense``

    Args:
        driver_license (:class:`telegram.api.types.inputIdentityDocument`):
            The driver license to be saved

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementDriverLicense"

    def __init__(self, driver_license, **kwargs):
        
        self.driver_license = driver_license  # InputIdentityDocument

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementDriverLicense":
        driver_license = Object.read(q.get('driver_license'))
        return InputPassportElementDriverLicense(driver_license)
