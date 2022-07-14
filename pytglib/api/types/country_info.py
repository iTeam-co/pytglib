

from ..utils import Object


class CountryInfo(Object):
    """
    Contains information about a country

    Attributes:
        ID (:obj:`str`): ``CountryInfo``

    Args:
        country_code (:obj:`str`):
            A two-letter ISO 3166-1 alpha-2 country code
        name (:obj:`str`):
            Native name of the country
        english_name (:obj:`str`):
            English name of the country
        is_hidden (:obj:`bool`):
            True, if the country must be hidden from the list of all countries
        calling_codes (List of :obj:`str`):
            List of country calling codes

    Returns:
        CountryInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "countryInfo"

    def __init__(self, country_code, name, english_name, is_hidden, calling_codes, **kwargs):
        
        self.country_code = country_code  # str
        self.name = name  # str
        self.english_name = english_name  # str
        self.is_hidden = is_hidden  # bool
        self.calling_codes = calling_codes  # list of str

    @staticmethod
    def read(q: dict, *args) -> "CountryInfo":
        country_code = q.get('country_code')
        name = q.get('name')
        english_name = q.get('english_name')
        is_hidden = q.get('is_hidden')
        calling_codes = q.get('calling_codes')
        return CountryInfo(country_code, name, english_name, is_hidden, calling_codes)
