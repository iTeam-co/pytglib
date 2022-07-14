

from ..utils import Object


class PhoneNumberInfo(Object):
    """
    Contains information about a phone number

    Attributes:
        ID (:obj:`str`): ``PhoneNumberInfo``

    Args:
        country (:class:`telegram.api.types.countryInfo`):
            Information about the country to which the phone number belongs; may be null
        country_calling_code (:obj:`str`):
            The part of the phone number denoting country calling code or its part
        formatted_phone_number (:obj:`str`):
            The phone number without country calling code formatted accordingly to local rulesExpected digits are returned as '-', but even more digits might be entered by the user

    Returns:
        PhoneNumberInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "phoneNumberInfo"

    def __init__(self, country, country_calling_code, formatted_phone_number, **kwargs):
        
        self.country = country  # CountryInfo
        self.country_calling_code = country_calling_code  # str
        self.formatted_phone_number = formatted_phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "PhoneNumberInfo":
        country = Object.read(q.get('country'))
        country_calling_code = q.get('country_calling_code')
        formatted_phone_number = q.get('formatted_phone_number')
        return PhoneNumberInfo(country, country_calling_code, formatted_phone_number)
