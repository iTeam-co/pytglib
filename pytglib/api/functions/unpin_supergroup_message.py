

from ..utils import Object


class UnpinSupergroupMessage(Object):
    """
    Removes the pinned message from a supergroup or channel; requires appropriate administrator rights in the supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``UnpinSupergroupMessage``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "unpinSupergroupMessage"

    def __init__(self, supergroup_id, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UnpinSupergroupMessage":
        supergroup_id = q.get('supergroup_id')
        return UnpinSupergroupMessage(supergroup_id)
