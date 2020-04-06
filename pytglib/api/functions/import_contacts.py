

from ..utils import Object


class ImportContacts(Object):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored 

    Attributes:
        ID (:obj:`str`): ``ImportContacts``

    Args:
        contacts (List of :class:`telegram.api.types.contact`):
            The list of contacts to import or edit; contacts' vCard are ignored and are not imported

    Returns:
        ImportedContacts

    Raises:
        :class:`telegram.Error`
    """
    ID = "importContacts"

    def __init__(self, contacts, extra=None, **kwargs):
        self.extra = extra
        self.contacts = contacts  # list of contact

    @staticmethod
    def read(q: dict, *args) -> "ImportContacts":
        contacts = [Object.read(i) for i in q.get('contacts', [])]
        return ImportContacts(contacts)
