

from ..utils import Object


class Sessions(Object):
    """
    Contains a list of sessions 

    Attributes:
        ID (:obj:`str`): ``Sessions``

    Args:
        sessions (List of :class:`telegram.api.types.session`):
            List of sessions 
        inactive_session_ttl_days (:obj:`int`):
            Number of days of inactivity before sessions will automatically be terminated; 1-366 days

    Returns:
        Sessions

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessions"

    def __init__(self, sessions, inactive_session_ttl_days, **kwargs):
        
        self.sessions = sessions  # list of session
        self.inactive_session_ttl_days = inactive_session_ttl_days  # int

    @staticmethod
    def read(q: dict, *args) -> "Sessions":
        sessions = [Object.read(i) for i in q.get('sessions', [])]
        inactive_session_ttl_days = q.get('inactive_session_ttl_days')
        return Sessions(sessions, inactive_session_ttl_days)
