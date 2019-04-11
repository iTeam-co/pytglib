

from ..utils import Object


class MessageChatUpgradeTo(Object):
    """
    A basic group was upgraded to a supergroup and was deactivated as the result 

    Attributes:
        ID (:obj:`str`): ``MessageChatUpgradeTo``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the supergroup to which the basic group was upgraded

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatUpgradeTo"

    def __init__(self, supergroup_id, **kwargs):
        
        self.supergroup_id = supergroup_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageChatUpgradeTo":
        supergroup_id = q.get('supergroup_id')
        return MessageChatUpgradeTo(supergroup_id)
