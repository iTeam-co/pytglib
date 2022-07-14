

from ..utils import Object


class ToggleSessionCanAcceptSecretChats(Object):
    """
    Toggles whether a session can accept incoming secret chats 

    Attributes:
        ID (:obj:`str`): ``ToggleSessionCanAcceptSecretChats``

    Args:
        session_id (:obj:`int`):
            Session identifier 
        can_accept_secret_chats (:obj:`bool`):
            Pass true to allow accepring secret chats by the session; pass false otherwise

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleSessionCanAcceptSecretChats"

    def __init__(self, session_id, can_accept_secret_chats, extra=None, **kwargs):
        self.extra = extra
        self.session_id = session_id  # int
        self.can_accept_secret_chats = can_accept_secret_chats  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleSessionCanAcceptSecretChats":
        session_id = q.get('session_id')
        can_accept_secret_chats = q.get('can_accept_secret_chats')
        return ToggleSessionCanAcceptSecretChats(session_id, can_accept_secret_chats)
