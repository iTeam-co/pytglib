

from ..utils import Object


class Call(Object):
    """
    Describes a call 

    Attributes:
        ID (:obj:`str`): ``Call``

    Args:
        id (:obj:`int`):
            Call identifier, not persistent 
        user_id (:obj:`int`):
            Peer user identifier 
        is_outgoing (:obj:`bool`):
            True, if the call is outgoing 
        state (:class:`telegram.api.types.CallState`):
            Call state

    Returns:
        Call

    Raises:
        :class:`telegram.Error`
    """
    ID = "call"

    def __init__(self, id, user_id, is_outgoing, state, **kwargs):
        
        self.id = id  # int
        self.user_id = user_id  # int
        self.is_outgoing = is_outgoing  # bool
        self.state = state  # CallState

    @staticmethod
    def read(q: dict, *args) -> "Call":
        id = q.get('id')
        user_id = q.get('user_id')
        is_outgoing = q.get('is_outgoing')
        state = Object.read(q.get('state'))
        return Call(id, user_id, is_outgoing, state)
