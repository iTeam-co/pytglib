

from ..utils import Object


class InternalLinkTypeUserPhoneNumber(Object):
    """
    The link is a link to a user by its phone number. Call searchUserByPhoneNumber with the given phone number to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeUserPhoneNumber``

    Args:
        phone_number (:obj:`str`):
            Phone number of the user

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeUserPhoneNumber"

    def __init__(self, phone_number, **kwargs):
        
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeUserPhoneNumber":
        phone_number = q.get('phone_number')
        return InternalLinkTypeUserPhoneNumber(phone_number)
