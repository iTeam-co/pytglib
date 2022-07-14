

from ..utils import Object


class InternalLinkTypePhoneNumberConfirmation(Object):
    """
    The link can be used to confirm ownership of a phone number to prevent account deletion. Call sendPhoneNumberConfirmationCode with the given hash and phone number to process the link

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypePhoneNumberConfirmation``

    Args:
        hash (:obj:`str`):
            Hash value from the link 
        phone_number (:obj:`str`):
            Phone number value from the link

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypePhoneNumberConfirmation"

    def __init__(self, hash, phone_number, **kwargs):
        
        self.hash = hash  # str
        self.phone_number = phone_number  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypePhoneNumberConfirmation":
        hash = q.get('hash')
        phone_number = q.get('phone_number')
        return InternalLinkTypePhoneNumberConfirmation(hash, phone_number)
