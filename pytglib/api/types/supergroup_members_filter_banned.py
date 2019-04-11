

from ..utils import Object


class SupergroupMembersFilterBanned(Object):
    """
    Returns users banned from the supergroup or channel; can be used only by administrators 

    Attributes:
        ID (:obj:`str`): ``SupergroupMembersFilterBanned``

    Args:
        query (:obj:`str`):
            Query to search for

    Returns:
        SupergroupMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "supergroupMembersFilterBanned"

    def __init__(self, query, **kwargs):
        
        self.query = query  # str

    @staticmethod
    def read(q: dict, *args) -> "SupergroupMembersFilterBanned":
        query = q.get('query')
        return SupergroupMembersFilterBanned(query)
