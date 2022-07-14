

from ..utils import Object


class GetPhoneNumberInfoSync(Object):
    """
    Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously

    Attributes:
        ID (:obj:`str`): ``GetPhoneNumberInfoSync``

    Args:
        language_code (:obj:`str`):
            A two-letter ISO 639-1 language code for country information localization 
        phone_number_prefix (:obj:`str`):
            The phone number prefix

    Returns:
        PhoneNumberInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPhoneNumberInfoSync"

    def __init__(self, language_code, phone_number_prefix, extra=None, **kwargs):
        self.extra = extra
        self.language_code = language_code  # str
        self.phone_number_prefix = phone_number_prefix  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPhoneNumberInfoSync":
        language_code = q.get('language_code')
        phone_number_prefix = q.get('phone_number_prefix')
        return GetPhoneNumberInfoSync(language_code, phone_number_prefix)
