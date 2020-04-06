

from ..utils import Object


class SupergroupMembersFilterContacts(Object):
    """
    Returns contacts of the user, which are members of the supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterContacts``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterContacts"

    def __init__(self, query, **kwargs):
        
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterContacts":
        query = q.get('query')
        return SupergroupMembersFilterContacts(query)
