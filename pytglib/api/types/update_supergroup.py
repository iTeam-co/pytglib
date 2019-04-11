

from ..utils import Object


class UpdateSupergroup(Object):
    """
    Some data of a supergroup or a channel has changed. This update is guaranteed to come before the supergroup identifier is returned to the client 

    Attributes:
        ID (:obj:`str`): ``UpdateSupergroup``

    Args:
        supergroup (:class:`telegram.api.types.supergroup`):
            New data about the supergroup

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSupergroup"

    def __init__(self, supergroup, **kwargs):
        
        self.supergroup = supergroup  # Supergroup

    @staticmethod
    def read(q: dict, *args) -> "UpdateSupergroup":
        supergroup = Object.read(q.get('supergroup'))
        return UpdateSupergroup(supergroup)
