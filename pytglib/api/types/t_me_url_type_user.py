

from ..utils import Object


class TMeUrlTypeUser(Object):
    """
    A URL linking to a user 

    Attributes:
        ID (:obj:`str`): ``TMeUrlTypeUser``

    Args:
        user_id (:obj:`int`):
            Identifier of the user

    Returns:
        TMeUrlType

    Raises:
        :class:`telegram.Error`
    """
    ID = "tMeUrlTypeUser"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "TMeUrlTypeUser":
        user_id = q.get('user_id')
        return TMeUrlTypeUser(user_id)
