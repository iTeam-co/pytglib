

from ..utils import Object


class SetInactiveSessionTtl(Object):
    """
    Changes the period of inactivity after which sessions will automatically be terminated 

    Attributes:
        ID (:obj:`str`): ``SetInactiveSessionTtl``

    Args:
        inactive_session_ttl_days (:obj:`int`):
            New number of days of inactivity before sessions will be automatically terminated; 1-366 days

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setInactiveSessionTtl"

    def __init__(self, inactive_session_ttl_days, extra=None, **kwargs):
        self.extra = extra
        self.inactive_session_ttl_days = inactive_session_ttl_days  # int

    @staticmethod
    def read(q: dict, *args) -> "SetInactiveSessionTtl":
        inactive_session_ttl_days = q.get('inactive_session_ttl_days')
        return SetInactiveSessionTtl(inactive_session_ttl_days)
