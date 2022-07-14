

from ..utils import Object


class ToggleSessionCanAcceptCalls(Object):
    """
    Toggles whether a session can accept incoming calls 

    Attributes:
        ID (:obj:`str`): ``ToggleSessionCanAcceptCalls``

    Args:
        session_id (:obj:`int`):
            Session identifier 
        can_accept_calls (:obj:`bool`):
            Pass true to allow accepting incoming calls by the session; pass false otherwise

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSessionCanAcceptCalls"

    def __init__(self, session_id, can_accept_calls, extra=None, **kwargs):
        self.extra = extra
        self.session_id = session_id  # int
        self.can_accept_calls = can_accept_calls  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSessionCanAcceptCalls":
        session_id = q.get('session_id')
        can_accept_calls = q.get('can_accept_calls')
        return ToggleSessionCanAcceptCalls(session_id, can_accept_calls)
