

from ..utils import Object


class GroupCallVideoSourceGroup(Object):
    """
    Describes a group of video synchronization source identifiers 

    Attributes:
        ID (:obj:`str`): ``GroupCallVideoSourceGroup``

    Args:
        semantics (:obj:`str`):
            The semantics of sources, one of "SIM" or "FID" 
        source_ids (List of :obj:`int`):
            The list of synchronization source identifiers

    Returns:
        GroupCallVideoSourceGroup

    Raises:
        :class:`telegram.Error`
    """
    ID = "groupCallVideoSourceGroup"

    def __init__(self, semantics, source_ids, **kwargs):
        
        self.semantics = semantics  # str
        self.source_ids = source_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "GroupCallVideoSourceGroup":
        semantics = q.get('semantics')
        source_ids = q.get('source_ids')
        return GroupCallVideoSourceGroup(semantics, source_ids)
