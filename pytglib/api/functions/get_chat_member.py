

from ..utils import Object


class GetChatMember(Object):
    """
    Returns information about a single member of a chat 

    Attributes:
        ID (:obj:`str`): ``GetChatMember``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        member_id (:class:`telegram.api.types.MessageSender`):
            Member identifier

    Returns:
        ChatMember

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatMember"

    def __init__(self, chat_id, member_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.member_id = member_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "GetChatMember":
        chat_id = q.get('chat_id')
        member_id = Object.read(q.get('member_id'))
        return GetChatMember(chat_id, member_id)
