

from ..utils import Object


class ImportedContacts(Object):
    """
    Represents the result of an ImportContacts request 

    Attributes:
        ID (:obj:`str`): ``ImportedContacts``

    Args:
        user_ids (List of :obj:`int`):
            User identifiers of the imported contacts in the same order as they were specified in the request; 0 if the contact is not yet a registered user
        importer_count (List of :obj:`int`):
            The number of users that imported the corresponding contact; 0 for already registered users or if unavailable

    Returns:
        ImportedContacts

    Raises:
        :class:`telegram.Error`
    """
    ID = "importedContacts"

    def __init__(self, user_ids, importer_count, **kwargs):
        
        self.user_ids = user_ids  # list of int
        self.importer_count = importer_count  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ImportedContacts":
        user_ids = q.get('user_ids')
        importer_count = q.get('importer_count')
        return ImportedContacts(user_ids, importer_count)
