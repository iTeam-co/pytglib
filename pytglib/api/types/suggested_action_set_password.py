

from ..utils import Object


class SuggestedActionSetPassword(Object):
    """
    Suggests the user to set a 2-step verification password to be able to log in again 

    Attributes:
        ID (:obj:`str`): ``SuggestedActionSetPassword``

    Args:
        authorization_delay (:obj:`int`):
            The number of days to pass between consecutive authorizations if the user declines to set password

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionSetPassword"

    def __init__(self, authorization_delay, **kwargs):
        
        self.authorization_delay = authorization_delay  # int

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionSetPassword":
        authorization_delay = q.get('authorization_delay')
        return SuggestedActionSetPassword(authorization_delay)
