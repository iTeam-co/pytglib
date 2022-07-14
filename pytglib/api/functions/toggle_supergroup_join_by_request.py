

from ..utils import Object


class ToggleSupergroupJoinByRequest(Object):
    """
    Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right 

    Attributes:
        ID (:obj:`str`): ``ToggleSupergroupJoinByRequest``

    Args:
        supergroup_id (:obj:`int`):
            Identifier of the channel 
        join_by_request (:obj:`bool`):
            New value of join_by_request

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSupergroupJoinByRequest"

    def __init__(self, supergroup_id, join_by_request, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.join_by_request = join_by_request  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSupergroupJoinByRequest":
        supergroup_id = q.get('supergroup_id')
        join_by_request = q.get('join_by_request')
        return ToggleSupergroupJoinByRequest(supergroup_id, join_by_request)
