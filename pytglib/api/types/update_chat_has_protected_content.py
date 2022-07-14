

from ..utils import Object


class UpdateChatHasProtectedContent(Object):
    """
    A chat content was allowed or restricted for saving 

    Attributes:
        ID (:obj:`str`): ``UpdateChatHasProtectedContent``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        has_protected_content (:obj:`bool`):
            New value of has_protected_content

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatHasProtectedContent"

    def __init__(self, chat_id, has_protected_content, **kwargs):
        
        self.chat_id = chat_id  # int
        self.has_protected_content = has_protected_content  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatHasProtectedContent":
        chat_id = q.get('chat_id')
        has_protected_content = q.get('has_protected_content')
        return UpdateChatHasProtectedContent(chat_id, has_protected_content)
