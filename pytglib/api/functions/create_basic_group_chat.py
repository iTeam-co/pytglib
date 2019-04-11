

from ..utils import Object


class CreateBasicGroupChat(Object):
    """
    Returns an existing chat corresponding to a known basic group 

    Attributes:
        ID (:obj:`str`): ``CreateBasicGroupChat``

    Args:
        basic_group_id (:obj:`int`):
            Basic group identifier 
        force (:obj:`bool`):
            If true, the chat will be created without network requestIn this case all information about the chat except its type, title and photo can be incorrect

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createBasicGroupChat"

    def __init__(self, basic_group_id, force, extra=None, **kwargs):
        self.extra = extra
        self.basic_group_id = basic_group_id  # int
        self.force = force  # bool

    @staticmethod
    def read(q: dict, *args) -> "CreateBasicGroupChat":
        basic_group_id = q.get('basic_group_id')
        force = q.get('force')
        return CreateBasicGroupChat(basic_group_id, force)
