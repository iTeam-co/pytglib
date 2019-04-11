

from ..utils import Object


class ChatTypeSupergroup(Object):
    """
    A supergroup (i.e. a chat with up to GetOption("supergroup_max_size") other users), or channel (with unlimited members) 

    Attributes:
        ID (:obj:`str`): ``ChatTypeSupergroup``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup or channel identifier 
        is_channel (:obj:`bool`):
            True, if the supergroup is a channel

    Returns:
        ChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatTypeSupergroup"

    def __init__(self, supergroup_id, is_channel, **kwargs):
        
        self.supergroup_id = supergroup_id  # int
        self.is_channel = is_channel  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatTypeSupergroup":
        supergroup_id = q.get('supergroup_id')
        is_channel = q.get('is_channel')
        return ChatTypeSupergroup(supergroup_id, is_channel)
