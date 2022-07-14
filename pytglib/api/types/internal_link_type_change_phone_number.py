

from ..utils import Object


class InternalLinkTypeChangePhoneNumber(Object):
    """
    The link is a link to the change phone number section of the app

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeChangePhoneNumber``

    No parameters required.

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeChangePhoneNumber"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeChangePhoneNumber":
        
        return InternalLinkTypeChangePhoneNumber()
