

from ..utils import Object


class ChangeImportedContacts(Object):
    """
    Changes imported contacts using the list of current user contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts.Query result depends on the result of the previous query, so only one query is possible at the same time 

    Attributes:
        ID (:obj:`str`): ``ChangeImportedContacts``

    Args:
        contacts (List of :class:`telegram.api.types.contact`):
            The new list of contacts, contact's vCard are ignored and are not imported

    Returns:
        ImportedContacts

    Raises:
        :class:`telegram.Error`
    """
    ID = "changeImportedContacts"

    def __init__(self, contacts, extra=None, **kwargs):
        self.extra = extra
        self.contacts = contacts  # list of contact

    @staticmethod
    def read(q: dict, *args) -> "ChangeImportedContacts":
        contacts = [Object.read(i) for i in q.get('contacts', [])]
        return ChangeImportedContacts(contacts)
