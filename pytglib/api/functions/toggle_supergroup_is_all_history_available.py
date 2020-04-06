

from ..utils import Object


class ToggleSupergroupIsAllHistoryAvailable(Object):
    """
    Toggles whether the message history of a supergroup is available to new members; requires can_change_info rights 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupIsAllHistoryAvailable``

    Args:
        supergroup_id (:obj:`int`):
            The identifier of the supergroup 
        is_all_history_available (:obj:`bool`):
            The new value of is_all_history_available

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupIsAllHistoryAvailable"

    def __init__(self, supergroup_id, is_all_history_available, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.is_all_history_available = is_all_history_available  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupIsAllHistoryAvailable":
        supergroup_id = q.get('supergroup_id')
        is_all_history_available = q.get('is_all_history_available')
        return ToggleSupergroupIsAllHistoryAvailable(supergroup_id, is_all_history_available)
