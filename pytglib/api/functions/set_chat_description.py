

from ..utils import Object


class SetChatDescription(Object):
    """
    Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info rights 

    Attributes:
        ID (:obj:`str`): ``SetChatDescription``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat 
        description (:obj:`str`):
            New chat description; 0-255 characters

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatDescription"

    def __init__(self, chat_id, description, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "SetChatDescription":
        chat_id = q.get('chat_id')
        description = q.get('description')
        return SetChatDescription(chat_id, description)
