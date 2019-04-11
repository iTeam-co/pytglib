

from ..utils import Object


class ChatTypeBasicGroup(Object):
    """
    A basic group (i.e., a chat with 0-200 other users) 

    Attributes:
        ID (:obj:`str`): ``ChatTypeBasicGroup``

    Args:
        basic_group_id (:obj:`int`):
            Basic group identifier

    Returns:
        ChatType

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatTypeBasicGroup"

    def __init__(self, basic_group_id, **kwargs):
        
        self.basic_group_id = basic_group_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatTypeBasicGroup":
        basic_group_id = q.get('basic_group_id')
        return ChatTypeBasicGroup(basic_group_id)
