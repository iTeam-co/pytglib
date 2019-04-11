

from ..utils import Object


class InputMessageContact(Object):
    """
    A message containing a user contact 

    Attributes:
        ID (:obj:`str`): ``InputMessageContact``

    Args:
        contact (:class:`telegram.api.types.contact`):
            Contact to send

    Returns:
        InputMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "inputMessageContact"

    def __init__(self, contact, **kwargs):
        
        self.contact = contact  # Contact

    @staticmethod
    def read(q: dict, *args) -> "InputMessageContact":
        contact = Object.read(q.get('contact'))
        return InputMessageContact(contact)
