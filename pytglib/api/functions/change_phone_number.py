

from ..utils import Object


class ChangePhoneNumber(Object):
    """
    Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code

    Attributes:
        ID (:obj:`str`): ``ChangePhoneNumber``

    Args:
        phone_number (:obj:`str`):
            The new phone number of the user in international format 
        allow_flash_call (:obj:`bool`):
            Pass true if the code can be sent via flash call to the specified phone number 
        is_current_phone_number (:obj:`bool`):
            Pass true if the phone number is used on the current deviceIgnored if allow_flash_call is false

    Returns:
        AuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "changePhoneNumber"

    def __init__(self, phone_number, allow_flash_call, is_current_phone_number, extra=None, **kwargs):
        self.extra = extra
        self.phone_number = phone_number  # str
        self.allow_flash_call = allow_flash_call  # bool
        self.is_current_phone_number = is_current_phone_number  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChangePhoneNumber":
        phone_number = q.get('phone_number')
        allow_flash_call = q.get('allow_flash_call')
        is_current_phone_number = q.get('is_current_phone_number')
        return ChangePhoneNumber(phone_number, allow_flash_call, is_current_phone_number)
