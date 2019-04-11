

from ..utils import Object


class MessageChatAddMembers(Object):
    """
    New chat members were added 

    Attributes:
        ID (:obj:`str`): ``MessageChatAddMembers``

    Args:
        member_user_ids (List of :obj:`int`):
            User identifiers of the new members

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatAddMembers"

    def __init__(self, member_user_ids, **kwargs):
        
        self.member_user_ids = member_user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "MessageChatAddMembers":
        member_user_ids = q.get('member_user_ids')
        return MessageChatAddMembers(member_user_ids)
