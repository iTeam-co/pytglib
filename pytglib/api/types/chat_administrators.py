

from ..utils import Object


class ChatAdministrators(Object):
    """
    Represents a list of chat administrators 

    Attributes:
        ID (:obj:`str`): ``ChatAdministrators``

    Args:
        administrators (List of :class:`telegram.api.types.chatAdministrator`):
            A list of chat administrators

    Returns:
        ChatAdministrators

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatAdministrators"

    def __init__(self, administrators, **kwargs):
        
        self.administrators = administrators  # list of chatAdministrator

    @staticmethod
    def read(q: dict, *args) -> "ChatAdministrators":
        administrators = [Object.read(i) for i in q.get('administrators', [])]
        return ChatAdministrators(administrators)
