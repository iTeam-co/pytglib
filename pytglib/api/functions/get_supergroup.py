

from ..utils import Object


class GetSupergroup(Object):
    """
    Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot 

    Attributes:
        ID (:obj:`str`): ``GetSupergroup``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup or channel identifier

    Returns:
        Supergroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "getSupergroup"

    def __init__(self, supergroup_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetSupergroup":
        supergroup_id = q.get('supergroup_id')
        return GetSupergroup(supergroup_id)
