

from ..utils import Object


class SuggestedActionCheckPassword(Object):
    """
    Suggests the user to check whether they still remember their 2-step verification password

    Attributes:
        ID (:obj:`str`): ``SuggestedActionCheckPassword``

    No parameters required.

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionCheckPassword"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionCheckPassword":
        
        return SuggestedActionCheckPassword()
