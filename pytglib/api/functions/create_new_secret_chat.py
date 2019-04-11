

from ..utils import Object


class CreateNewSecretChat(Object):
    """
    Creates a new secret chat. Returns the newly created chat 

    Attributes:
        ID (:obj:`str`): ``CreateNewSecretChat``

    Args:
        user_id (:obj:`int`):
            Identifier of the target user

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewSecretChat"

    def __init__(self, user_id, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "CreateNewSecretChat":
        user_id = q.get('user_id')
        return CreateNewSecretChat(user_id)
