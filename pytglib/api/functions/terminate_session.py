

from ..utils import Object


class TerminateSession(Object):
    """
    Terminates a session of the current user 

    Attributes:
        ID (:obj:`str`): ``TerminateSession``

    Args:
        session_id (:obj:`int`):
            Session identifier

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "terminateSession"

    def __init__(self, session_id, extra=None, **kwargs):
        self.extra = extra
        self.session_id = session_id  # int

    @staticmethod
    def read(q: dict, *args) -> "TerminateSession":
        session_id = q.get('session_id')
        return TerminateSession(session_id)
