

from ..utils import Object


class PassportElementPersonalDetails(Object):
    """
    A Telegram Passport element containing the user's personal details 

    Attributes:
        ID (:obj:`str`): ``PassportElementPersonalDetails``

    Args:
        personal_details (:class:`telegram.api.types.personalDetails`):
            Personal details of the user

    Returns:
        PassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "passportElementPersonalDetails"

    def __init__(self, personal_details, **kwargs):
        
        self.personal_details = personal_details  # PersonalDetails

    @staticmethod
    def read(q: dict, *args) -> "PassportElementPersonalDetails":
        personal_details = Object.read(q.get('personal_details'))
        return PassportElementPersonalDetails(personal_details)
