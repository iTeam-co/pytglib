

from ..utils import Object


class SetChatMemberStatus(Object):
    """
    Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead. Use addChatMember or banChatMember if some additional parameters needs to be passed

    Attributes:
        ID (:obj:`str`): ``SetChatMemberStatus``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        member_id (:class:`telegram.api.types.MessageSender`):
            Member identifierChats can be only banned and unbanned in supergroups and channels 
        status (:class:`telegram.api.types.ChatMemberStatus`):
            The new status of the member in the chat

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatMemberStatus"

    def __init__(self, chat_id, member_id, status, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.member_id = member_id  # MessageSender
        self.status = status  # ChatMemberStatus

    @staticmethod
    def read(q: dict, *args) -> "SetChatMemberStatus":
        chat_id = q.get('chat_id')
        member_id = Object.read(q.get('member_id'))
        status = Object.read(q.get('status'))
        return SetChatMemberStatus(chat_id, member_id, status)
