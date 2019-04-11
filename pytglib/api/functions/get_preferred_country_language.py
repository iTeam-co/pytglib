

from ..utils import Object


class GetPreferredCountryLanguage(Object):
    """
    Returns an IETF language tag of the language preferred in the country, which should be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown 

    Attributes:
        ID (:obj:`str`): ``GetPreferredCountryLanguage``

    Args:
        country_code (:obj:`str`):
            A two-letter ISO 3166-1 alpha-2 country code

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPreferredCountryLanguage"

    def __init__(self, country_code, extra=None, **kwargs):
        self.extra = extra
        self.country_code = country_code  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPreferredCountryLanguage":
        country_code = q.get('country_code')
        return GetPreferredCountryLanguage(country_code)
