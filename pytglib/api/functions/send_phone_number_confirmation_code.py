

from ..utils import Object


class SendPhoneNumberConfirmationCode(Object):
    """
    Sends phone number confirmation code. Should be called when user presses "https://t.me/confirmphone?phone=*******&hash=**********" or "tg://confirmphone?phone=*******&hash=**********" link 

    Attributes:
        ID (:obj:`str`): ``SendPhoneNumberConfirmationCode``

    Args:
        hash (:obj:`str`):
            Value of the "hash" parameter from the link
        phone_number (:obj:`str`):
            Value of the "phone" parameter from the link 
        allow_flash_call (:obj:`bool`):
            Pass true if the authentication code may be sent via flash call to the specified phone number 
        is_current_phone_number (:obj:`bool`):
            Pass true if the phone number is used on the current deviceIgnored if allow_flash_call is false

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPhoneNumberConfirmationCode"

    def __init__(self, hash, phone_number, allow_flash_call, is_current_phone_number, extra=None, **kwargs):
        self.extra = extra
        self.hash = hash  # str
        self.phone_number = phone_number  # str
        self.allow_flash_call = allow_flash_call  # bool
        self.is_current_phone_number = is_current_phone_number  # bool

    @staticmethod
    def read(q: dict, *args) -> "SendPhoneNumberConfirmationCode":
        hash = q.get('hash')
        phone_number = q.get('phone_number')
        allow_flash_call = q.get('allow_flash_call')
        is_current_phone_number = q.get('is_current_phone_number')
        return SendPhoneNumberConfirmationCode(hash, phone_number, allow_flash_call, is_current_phone_number)
