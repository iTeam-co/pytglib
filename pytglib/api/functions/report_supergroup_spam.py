

from ..utils import Object


class ReportSupergroupSpam(Object):
    """
    Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup 

    Attributes:
        ID (:obj:`str`): ``ReportSupergroupSpam``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup identifier 
        user_id (:obj:`int`):
            User identifier 
        message_ids (List of :obj:`int`):
            Identifiers of messages sent in the supergroup by the userThis list must be non-empty

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reportSupergroupSpam"

    def __init__(self, supergroup_id, user_id, message_ids, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.user_id = user_id  # int
        self.message_ids = message_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ReportSupergroupSpam":
        supergroup_id = q.get('supergroup_id')
        user_id = q.get('user_id')
        message_ids = q.get('message_ids')
        return ReportSupergroupSpam(supergroup_id, user_id, message_ids)
