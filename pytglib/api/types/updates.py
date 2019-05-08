

from ..utils import Object


class Updates(Object):
    """
    Contains a list of updates 

    Attributes:
        ID (:obj:`str`): ``Updates``

    Args:
        updates (List of :class:`telegram.api.types.Update`):
            List of updates

    Returns:
        Updates

    Raises:
        :class:`telegram.Error`
    """
    ID = "updates"

    def __init__(self, updates, **kwargs):
        
        self.updates = updates  # list of Update

    @staticmethod
    def read(q: dict, *args) -> "Updates":
        updates = [Object.read(i) for i in q.get('updates', [])]
        return Updates(updates)
