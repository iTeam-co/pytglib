

from ..utils import Object


class EmailAddressAuthenticationCodeInfo(Object):
    """
    Information about the email address authentication code that was sent 

    Attributes:
        ID (:obj:`str`): ``EmailAddressAuthenticationCodeInfo``

    Args:
        email_address_pattern (:obj:`str`):
            Pattern of the email address to which an authentication code was sent 
        length (:obj:`int`):
            Length of the code; 0 if unknown

    Returns:
        EmailAddressAuthenticationCodeInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "emailAddressAuthenticationCodeInfo"

    def __init__(self, email_address_pattern, length, **kwargs):
        
        self.email_address_pattern = email_address_pattern  # str
        self.length = length  # int

    @staticmethod
    def read(q: dict, *args) -> "EmailAddressAuthenticationCodeInfo":
        email_address_pattern = q.get('email_address_pattern')
        length = q.get('length')
        return EmailAddressAuthenticationCodeInfo(email_address_pattern, length)
