

from ..utils import Object


class Sessions(Object):
    """
    Contains a list of sessions 

    Attributes:
        ID (:obj:`str`): ``Sessions``

    Args:
        sessions (List of :class:`telegram.api.types.session`):
            List of sessions

    Returns:
        Sessions

    Raises:
        :class:`telegram.Error`
    """
    ID = "sessions"

    def __init__(self, sessions, **kwargs):
        
        self.sessions = sessions  # list of session

    @staticmethod
    def read(q: dict, *args) -> "Sessions":
        sessions = [Object.read(i) for i in q.get('sessions', [])]
        return Sessions(sessions)
