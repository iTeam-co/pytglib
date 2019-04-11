

from ..utils import Object


class CreatePrivateChat(Object):
    """
    Returns an existing chat corresponding to a given user 

    Attributes:
        ID (:obj:`str`): ``CreatePrivateChat``

    Args:
        user_id (:obj:`int`):
            User identifier 
        force (:obj:`bool`):
            If true, the chat will be created without network requestIn this case all information about the chat except its type, title and photo can be incorrect

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createPrivateChat"

    def __init__(self, user_id, force, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.force = force  # bool

    @staticmethod
    def read(q: dict, *args) -> "CreatePrivateChat":
        user_id = q.get('user_id')
        force = q.get('force')
        return CreatePrivateChat(user_id, force)
