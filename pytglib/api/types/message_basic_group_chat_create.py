

from ..utils import Object


class MessageBasicGroupChatCreate(Object):
    """
    A newly created basic group 

    Attributes:
        ID (:obj:`str`): ``MessageBasicGroupChatCreate``

    Args:
        title (:obj:`str`):
            Title of the basic group 
        member_user_ids (List of :obj:`int`):
            User identifiers of members in the basic group

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageBasicGroupChatCreate"

    def __init__(self, title, member_user_ids, **kwargs):
        
        self.title = title  # str
        self.member_user_ids = member_user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "MessageBasicGroupChatCreate":
        title = q.get('title')
        member_user_ids = q.get('member_user_ids')
        return MessageBasicGroupChatCreate(title, member_user_ids)
