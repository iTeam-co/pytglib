

from ..utils import Object


class SetSupergroupUsername(Object):
    """
    Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``SetSupergroupUsername``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup or channel 
        username (:obj:`str`):
            New value of the usernameUse an empty string to remove the username

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setSupergroupUsername"

    def __init__(self, supergroup_id, username, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.username = username  # str

    @staticmethod
    def read(q: dict, *args) -> "SetSupergroupUsername":
        supergroup_id = q.get('supergroup_id')
        username = q.get('username')
        return SetSupergroupUsername(supergroup_id, username)
