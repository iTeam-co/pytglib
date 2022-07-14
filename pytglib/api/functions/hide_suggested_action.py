

from ..utils import Object


class HideSuggestedAction(Object):
    """
    Hides a suggested action 

    Attributes:
        ID (:obj:`str`): ``HideSuggestedAction``

    Args:
        action (:class:`telegram.api.types.SuggestedAction`):
            Suggested action to hide

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "hideSuggestedAction"

    def __init__(self, action, extra=None, **kwargs):
        self.extra = extra
        self.action = action  # SuggestedAction

    @staticmethod
    def read(q: dict, *args) -> "HideSuggestedAction":
        action = Object.read(q.get('action'))
        return HideSuggestedAction(action)
