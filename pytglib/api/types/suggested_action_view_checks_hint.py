

from ..utils import Object


class SuggestedActionViewChecksHint(Object):
    """
    Suggests the user to view a hint about the meaning of one and two check marks on sent messages

    Attributes:
        ID (:obj:`str`): ``SuggestedActionViewChecksHint``

    No parameters required.

    Returns:
        SuggestedAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "suggestedActionViewChecksHint"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SuggestedActionViewChecksHint":
        
        return SuggestedActionViewChecksHint()
