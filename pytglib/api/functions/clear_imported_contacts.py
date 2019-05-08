

from ..utils import Object


class ClearImportedContacts(Object):
    """
    Clears all imported contacts, contact list remains unchanged

    Attributes:
        ID (:obj:`str`): ``ClearImportedContacts``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "clearImportedContacts"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "ClearImportedContacts":
        
        return ClearImportedContacts()
