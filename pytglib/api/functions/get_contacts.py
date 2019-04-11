

from ..utils import Object


class GetContacts(Object):
    """
    Returns all user contacts

    Attributes:
        ID (:obj:`str`): ``GetContacts``

    No parameters required.

    Returns:
        Users

    Raises:
        :class:`telegram.Error`
    """
    ID = "getContacts"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "GetContacts":
        
        return GetContacts()
