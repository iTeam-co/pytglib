

from ..utils import Object


class ToggleChatHasProtectedContent(Object):
    """
    Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges

    Attributes:
        ID (:obj:`str`): ``ToggleChatHasProtectedContent``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        has_protected_content (:obj:`bool`):
            New value of has_protected_content

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleChatHasProtectedContent"

    def __init__(self, chat_id, has_protected_content, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.has_protected_content = has_protected_content  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleChatHasProtectedContent":
        chat_id = q.get('chat_id')
        has_protected_content = q.get('has_protected_content')
        return ToggleChatHasProtectedContent(chat_id, has_protected_content)
