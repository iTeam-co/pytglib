

from ..utils import Object


class SetUsername(Object):
    """
    Changes the username of the current user. If something changes, updateUser will be sent 

    Attributes:
        ID (:obj:`str`): ``SetUsername``

    Args:
        username (:obj:`str`):
            The new value of the usernameUse an empty string to remove the username

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setUsername"

    def __init__(self, username, extra=None, **kwargs):
        self.extra = extra
        self.username = username  # str

    @staticmethod
    def read(q: dict, *args) -> "SetUsername":
        username = q.get('username')
        return SetUsername(username)
