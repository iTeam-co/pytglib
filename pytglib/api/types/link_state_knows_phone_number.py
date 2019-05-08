

from ..utils import Object


class LinkStateKnowsPhoneNumber(Object):
    """
    The phone number of user A is known but that number has not been saved to the contact list of user B

    Attributes:
        ID (:obj:`str`): ``LinkStateKnowsPhoneNumber``

    No parameters required.

    Returns:
        LinkState

    Raises:
        :class:`telegram.Error`
    """
    ID = "linkStateKnowsPhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LinkStateKnowsPhoneNumber":
        
        return LinkStateKnowsPhoneNumber()
