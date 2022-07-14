

from ..utils import Object


class SearchUserByPhoneNumber(Object):
    """
    Searches a user by their phone number. Returns a 404 error if the user can't be found 

    Attributes:
        ID (:obj:`str`): ``SearchUserByPhoneNumber``

    Args:
        phone_number (:obj:`str`):
            Phone number to search for

    Returns:
        User

    Raises:
        :class:`telegram.Error`
    """
    ID = "searchUserByPhoneNumber"

    def __init__(self, phone_number, extra=None, **kwargs):
        self.extra = extra
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "SearchUserByPhoneNumber":
        phone_number = q.get('phone_number')
        return SearchUserByPhoneNumber(phone_number)
