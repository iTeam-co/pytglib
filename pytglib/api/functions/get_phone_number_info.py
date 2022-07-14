

from ..utils import Object


class GetPhoneNumberInfo(Object):
    """
    Returns information about a phone number by its prefix. Can be called before authorization 

    Attributes:
        ID (:obj:`str`): ``GetPhoneNumberInfo``

    Args:
        phone_number_prefix (:obj:`str`):
            The phone number prefix

    Returns:
        PhoneNumberInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPhoneNumberInfo"

    def __init__(self, phone_number_prefix, extra=None, **kwargs):
        self.extra = extra
        self.phone_number_prefix = phone_number_prefix  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPhoneNumberInfo":
        phone_number_prefix = q.get('phone_number_prefix')
        return GetPhoneNumberInfo(phone_number_prefix)
