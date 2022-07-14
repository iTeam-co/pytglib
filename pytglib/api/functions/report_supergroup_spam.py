

from ..utils import Object


class ReportSupergroupSpam(Object):
    """
    Reports messages in a supergroup as spam; requires administrator rights in the supergroup 

    Attributes:
        ID (:obj:`str`): ``ReportSupergroupSpam``

    Args:
        supergroup_id (:obj:`int`):
            Supergroup identifier 
        message_ids (List of :obj:`int`):
            Identifiers of messages to report

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reportSupergroupSpam"

    def __init__(self, supergroup_id, message_ids, extra=None, **kwargs):
        self.extra = extra
        self.supergroup_id = supergroup_id  # int
        self.message_ids = message_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ReportSupergroupSpam":
        supergroup_id = q.get('supergroup_id')
        message_ids = q.get('message_ids')
        return ReportSupergroupSpam(supergroup_id, message_ids)
