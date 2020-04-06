

from ..utils import Object


class MessageContact(Object):
    """
    A message with a user contact 

    Attributes:
        ID (:obj:`str`): ``MessageContact``

    Args:
        contact (:class:`telegram.api.types.contact`):
            The contact description

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageContact"

    def __init__(self, contact, **kwargs):
        
        self.contact = contact  # Contact

    @staticmethod
    def read(q: dict, *args) -> "MessageContact":
        contact = Object.read(q.get('contact'))
        return MessageContact(contact)
