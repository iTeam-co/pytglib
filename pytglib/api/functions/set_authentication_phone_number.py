

from ..utils import Object


class SetAuthenticationPhoneNumber(Object):
    """
    Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber,or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

    Attributes:
        ID (:obj:`str`): ``SetAuthenticationPhoneNumber``

    Args:
        phone_number (:obj:`str`):
            The phone number of the user, in international format 
        settings (:class:`telegram.api.types.phoneNumberAuthenticationSettings`):
            Settings for the authentication of the user's phone number

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setAuthenticationPhoneNumber"

    def __init__(self, phone_number, settings, extra=None, **kwargs):
        self.extra = extra
        self.phone_number = phone_number  # str
        self.settings = settings  # PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict, *args) -> "SetAuthenticationPhoneNumber":
        phone_number = q.get('phone_number')
        settings = Object.read(q.get('settings'))
        return SetAuthenticationPhoneNumber(phone_number, settings)
