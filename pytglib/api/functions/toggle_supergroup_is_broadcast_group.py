

from ..utils import Object


class ToggleSupergroupIsBroadcastGroup(Object):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupIsBroadcastGroup``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupIsBroadcastGroup"

    def __init__(self, supergroup_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupIsBroadcastGroup":
        supergroup_id = q.get('supergroup_id')
        return ToggleSupergroupIsBroadcastGroup(supergroup_id)
