

from ..utils import Object


class PhoneNumberAuthenticationSettings(Object):
    """
    Contains settings for the authentication of the user's phone number

    Attributes:
        ID (:obj:`str`): ``PhoneNumberAuthenticationSettings``

    Args:
        allow_flash_call (:obj:`bool`):
            Pass true if the authentication code may be sent via flash call to the specified phone number
        is_current_phone_number (:obj:`bool`):
            Pass true if the authenticated phone number is used on the current device
        allow_sms_retriever_api (:obj:`bool`):
            For official applications onlyTrue, if the app can use Android SMS Retriever API (requires Google Play Services >= 102) to automatically receive the authentication code from the SMSSee https://developersgooglecom/identity/sms-retriever/ for more details

    Returns:
        PhoneNumberAuthenticationSettings

    Raises:
        :class:`telegram.Error`
    """
    ID = "phoneNumberAuthenticationSettings"

    def __init__(self, allow_flash_call, is_current_phone_number, allow_sms_retriever_api, **kwargs):
        
        self.allow_flash_call = allow_flash_call  # bool
        self.is_current_phone_number = is_current_phone_number  # bool
        self.allow_sms_retriever_api = allow_sms_retriever_api  # bool

    @staticmethod
    def read(q: dict, *args) -> "PhoneNumberAuthenticationSettings":
        allow_flash_call = q.get('allow_flash_call')
        is_current_phone_number = q.get('is_current_phone_number')
        allow_sms_retriever_api = q.get('allow_sms_retriever_api')
        return PhoneNumberAuthenticationSettings(allow_flash_call, is_current_phone_number, allow_sms_retriever_api)
