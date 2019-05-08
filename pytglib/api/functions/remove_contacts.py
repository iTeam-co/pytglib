

from ..utils import Object


class RemoveContacts(Object):
    """
    Removes users from the contact list 

    Attributes:
        ID (:obj:`str`): ``RemoveContacts``

    Args:
        user_ids (List of :obj:`int`):
            Identifiers of users to be deleted

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeContacts"

    def __init__(self, user_ids, extra=None, **kwargs):
        self.extra = extra
        self.user_ids = user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "RemoveContacts":
        user_ids = q.get('user_ids')
        return RemoveContacts(user_ids)
