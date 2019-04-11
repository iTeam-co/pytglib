

from ..utils import Object


class MessageChatUpgradeFrom(Object):
    """
    A supergroup has been created from a basic group 

    Attributes:
        ID (:obj:`str`): ``MessageChatUpgradeFrom``

    Args:
        title (:obj:`str`):
            Title of the newly created supergroup 
        basic_group_id (:obj:`int`):
            The identifier of the original basic group

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatUpgradeFrom"

    def __init__(self, title, basic_group_id, **kwargs):
        
        self.title = title  # str
        self.basic_group_id = basic_group_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageChatUpgradeFrom":
        title = q.get('title')
        basic_group_id = q.get('basic_group_id')
        return MessageChatUpgradeFrom(title, basic_group_id)
