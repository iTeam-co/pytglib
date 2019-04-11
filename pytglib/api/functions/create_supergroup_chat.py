

from ..utils import Object


class CreateSupergroupChat(Object):
    """
    Returns an existing chat corresponding to a known supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``CreateSupergroupChat``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup or channel identifier 
        force (:obj:`bool`):
            If true, the chat will be created without network requestIn this case all information about the chat except its type, title and photo can be incorrect

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createSupergroupChat"

    def __init__(self, supergroup_id, force, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.force = force  # bool

    @staticmethod
    def read(q: dict, *args) -> "CreateSupergroupChat":
        supergroup_id = q.get('supergroup_id')
        force = q.get('force')
        return CreateSupergroupChat(supergroup_id, force)
