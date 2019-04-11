

from ..utils import Object


class SetSupergroupDescription(Object):
    """
    Changes information about a supergroup or channel; requires appropriate administrator rights 

    Attributes:
        ID (:obj:`str`): ``SetSupergroupDescription``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel 
        description (:obj:`str`):
            New supergroup or channel description; 0-255 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setSupergroupDescription"

    def __init__(self, supergroup_id, description, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "SetSupergroupDescription":
        supergroup_id = q.get('supergroup_id')
        description = q.get('description')
        return SetSupergroupDescription(supergroup_id, description)
