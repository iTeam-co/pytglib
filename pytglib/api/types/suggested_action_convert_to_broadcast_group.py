

from ..utils import Object


class SuggestedActionConvertToBroadcastGroup(Object):
    """
    Suggests the user to convert specified supergroup to a broadcast group 

    Attributes:
        ID (:obj:`str`): ``SuggestedActionConvertToBroadcastGroup``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup identifier

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionConvertToBroadcastGroup"

    def __init__(self, supergroup_id, **kwargs):
        
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionConvertToBroadcastGroup":
        supergroup_id = q.get('supergroup_id')
        return SuggestedActionConvertToBroadcastGroup(supergroup_id)
