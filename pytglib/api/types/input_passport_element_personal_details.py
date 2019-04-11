

from ..utils import Object


class InputPassportElementPersonalDetails(Object):
    """
    A Telegram Passport element to be saved containing the user's personal details 

    Attributes:
        ID (:obj:`str`): ``InputPassportElementPersonalDetails``

    Args:
        personal_details (:class:`telegram.api.types.personalDetails`):
            Personal details of the user

    Returns:
        InputPassportElement

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputPassportElementPersonalDetails"

    def __init__(self, personal_details, **kwargs):
        
        self.personal_details = personal_details  # PersonalDetails

    @staticmethod
    def read(q: dict, *args) -> "InputPassportElementPersonalDetails":
        personal_details = Object.read(q.get('personal_details'))
        return InputPassportElementPersonalDetails(personal_details)
