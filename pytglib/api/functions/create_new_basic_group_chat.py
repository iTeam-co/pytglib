

from ..utils import Object


class CreateNewBasicGroupChat(Object):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat 

    Attributes:
        ID (:obj:`str`): ``CreateNewBasicGroupChat``

    Args:
        user_ids (List of :obj:`int`):
            Identifiers of users to be added to the basic group 
        title (:obj:`str`):
            Title of the new basic group; 1-128 characters

    Returns:
        Chat

    Raises:
        :class:`telegram.Error`
    """
    ID = "createNewBasicGroupChat"

    def __init__(self, user_ids, title, extra=None, **kwargs):
        self.extra = extra
        self.user_ids = user_ids  # list of int
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "CreateNewBasicGroupChat":
        user_ids = q.get('user_ids')
        title = q.get('title')
        return CreateNewBasicGroupChat(user_ids, title)
