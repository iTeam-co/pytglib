

from ..utils import Object


class ChatEventIsAllHistoryAvailableToggled(Object):
    """
    The is_all_history_available setting of a supergroup was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventIsAllHistoryAvailableToggled``

    Args:
        is_all_history_available (:obj:`bool`):
            New value of is_all_history_available

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventIsAllHistoryAvailableToggled"

    def __init__(self, is_all_history_available, **kwargs):
        
        self.is_all_history_available = is_all_history_available  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventIsAllHistoryAvailableToggled":
        is_all_history_available = q.get('is_all_history_available')
        return ChatEventIsAllHistoryAvailableToggled(is_all_history_available)
