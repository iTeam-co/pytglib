

from ..utils import Object


class SetChatMemberStatus(Object):
    """
    Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for adding new members to the chat and transferring chat ownership; instead, use addChatMember or transferChatOwnership. The chat member status will not be changed until it has been synchronized with the server

    Attributes:
        ID (:obj:`str`): ``SetChatMemberStatus``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            User identifier 
        status (:class:`telegram.api.types.ChatMemberStatus`):
            The new status of the member in the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatMemberStatus"

    def __init__(self, chat_id, user_id, status, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.status = status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "SetChatMemberStatus":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        status = Object.read(q.get('status'))
        return SetChatMemberStatus(chat_id, user_id, status)
