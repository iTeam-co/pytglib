

from ..utils import Object


class TMeUrlTypeSupergroup(Object):
    """
    A URL linking to a public supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``TMeUrlTypeSupergroup``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel

    Returns:
        TMeUrlType

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrlTypeSupergroup"

    def __init__(self, supergroup_id, **kwargs):
        
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "TMeUrlTypeSupergroup":
        supergroup_id = q.get('supergroup_id')
        return TMeUrlTypeSupergroup(supergroup_id)
