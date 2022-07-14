

from ..utils import Object


class ChatEventHasProtectedContentToggled(Object):
    """
    The has_protected_content setting of a channel was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventHasProtectedContentToggled``

    Args:
        has_protected_content (:obj:`bool`):
            New value of has_protected_content

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventHasProtectedContentToggled"

    def __init__(self, has_protected_content, **kwargs):
        
        self.has_protected_content = has_protected_content  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventHasProtectedContentToggled":
        has_protected_content = q.get('has_protected_content')
        return ChatEventHasProtectedContentToggled(has_protected_content)
