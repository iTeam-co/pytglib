

from ..utils import Object


class GetSupergroupFullInfo(Object):
    """
    Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute 

    Attributes:
        ID (:obj:`str`): ``GetSupergroupFullInfo``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup or channel identifier

    Returns:
        SupergroupFullInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSupergroupFullInfo"

    def __init__(self, supergroup_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetSupergroupFullInfo":
        supergroup_id = q.get('supergroup_id')
        return GetSupergroupFullInfo(supergroup_id)
