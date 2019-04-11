

from ..utils import Object


class Contact(Object):
    """
    Describes a user contact 

    Attributes:
        ID (:obj:`str`): ``Contact``

    Args:
        phone_number (:obj:`str`):
            Phone number of the user 
        first_name (:obj:`str`):
            First name of the user; 1-255 characters in length 
        last_name (:obj:`str`):
            Last name of the user 
        vcard (:obj:`str`):
            Additional data about the user in a form of vCard; 0-2048 bytes in length 
        user_id (:obj:`int`):
            Identifier of the user, if known; otherwise 0

    Returns:
        Contact

    Raises:
        :class:`telegram.Error`
    """
    ID = "contact"

    def __init__(self, phone_number, first_name, last_name, vcard, user_id, **kwargs):
        
        self.phone_number = phone_number  # str
        self.first_name = first_name  # str
        self.last_name = last_name  # str
        self.vcard = vcard  # str
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "Contact":
        phone_number = q.get('phone_number')
        first_name = q.get('first_name')
        last_name = q.get('last_name')
        vcard = q.get('vcard')
        user_id = q.get('user_id')
        return Contact(phone_number, first_name, last_name, vcard, user_id)
