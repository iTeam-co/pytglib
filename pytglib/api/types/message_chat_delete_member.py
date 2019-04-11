

from ..utils import Object


class MessageChatDeleteMember(Object):
    """
    A chat member was deleted 

    Attributes:
        ID (:obj:`str`): ``MessageChatDeleteMember``

    Args:
        user_id (:obj:`int`):
            User identifier of the deleted chat member

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatDeleteMember"

    def __init__(self, user_id, **kwargs):
        
        self.user_id = user_id  # int

    @staticmethod
    def read(q: dict, *args) -> "MessageChatDeleteMember":
        user_id = q.get('user_id')
        return MessageChatDeleteMember(user_id)
