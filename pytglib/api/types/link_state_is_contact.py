

from ..utils import Object


class LinkStateIsContact(Object):
    """
    The phone number of user A has been saved to the contact list of user B

    Attributes:
        ID (:obj:`str`): ``LinkStateIsContact``

    No parameters required.

    Returns:
        LinkState

    Raises:
        :class:`telegram.Error`
    """
    ID = "linkStateIsContact"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LinkStateIsContact":
        
        return LinkStateIsContact()
