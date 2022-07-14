

from ..utils import Object


class GetChatInviteLink(Object):
    """
    Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

    Attributes:
        ID (:obj:`str`): ``GetChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier
        invite_link (:obj:`str`):
            Invite link to get

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatInviteLink"

    def __init__(self, chat_id, invite_link, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.invite_link = invite_link  # str

    @staticmethod
    def read(q: dict, *args) -> "GetChatInviteLink":
        chat_id = q.get('chat_id')
        invite_link = q.get('invite_link')
        return GetChatInviteLink(chat_id, invite_link)
