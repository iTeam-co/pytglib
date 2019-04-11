

from ..utils import Object


class PersonalDetails(Object):
    """
    Contains the user's personal details

    Attributes:
        ID (:obj:`str`): ``PersonalDetails``

    Args:
        first_name (:obj:`str`):
            First name of the user written in English; 1-255 characters 
        middle_name (:obj:`str`):
            Middle name of the user written in English; 0-255 characters 
        last_name (:obj:`str`):
            Last name of the user written in English; 1-255 characters
        native_first_name (:obj:`str`):
            Native first name of the user; 1-255 characters 
        native_middle_name (:obj:`str`):
            Native middle name of the user; 0-255 characters 
        native_last_name (:obj:`str`):
            Native last name of the user; 1-255 characters
        birthdate (:class:`telegram.api.types.date`):
            Birthdate of the user 
        gender (:obj:`str`):
            Gender of the user, "male" or "female" 
        country_code (:obj:`str`):
            A two-letter ISO 3166-1 alpha-2 country code of the user's country 
        residence_country_code (:obj:`str`):
            A two-letter ISO 3166-1 alpha-2 country code of the user's residence country

    Returns:
        PersonalDetails

    Raises:
        :class:`telegram.Error`
    """
    ID = "personalDetails"

    def __init__(self, first_name, middle_name, last_name, native_first_name, native_middle_name, native_last_name, birthdate, gender, country_code, residence_country_code, **kwargs):
        
        self.first_name = first_name  # str
        self.middle_name = middle_name  # str
        self.last_name = last_name  # str
        self.native_first_name = native_first_name  # str
        self.native_middle_name = native_middle_name  # str
        self.native_last_name = native_last_name  # str
        self.birthdate = birthdate  # Date
        self.gender = gender  # str
        self.country_code = country_code  # str
        self.residence_country_code = residence_country_code  # str

    @staticmethod
    def read(q: dict, *args) -> "PersonalDetails":
        first_name = q.get('first_name')
        middle_name = q.get('middle_name')
        last_name = q.get('last_name')
        native_first_name = q.get('native_first_name')
        native_middle_name = q.get('native_middle_name')
        native_last_name = q.get('native_last_name')
        birthdate = Object.read(q.get('birthdate'))
        gender = q.get('gender')
        country_code = q.get('country_code')
        residence_country_code = q.get('residence_country_code')
        return PersonalDetails(first_name, middle_name, last_name, native_first_name, native_middle_name, native_last_name, birthdate, gender, country_code, residence_country_code)
