

from ..utils import Object


class GenerateChatInviteLink(Object):
    """
    Generates a new invite link for a chat; the previously generated link is revoked. Available for basic groups, supergroups, and channels. In basic groups this can be called only by the group's creator; in supergroups and channels this requires appropriate administrator rights 

    Attributes:
        ID (:obj:`str`): ``GenerateChatInviteLink``

    Args:
        chat_id (:obj:`int`):
            Chat identifier

    Returns:
        ChatInviteLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "generateChatInviteLink"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GenerateChatInviteLink":
        chat_id = q.get('chat_id')
        return GenerateChatInviteLink(chat_id)
