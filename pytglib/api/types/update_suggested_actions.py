

from ..utils import Object


class UpdateSuggestedActions(Object):
    """
    The list of suggested to the user actions has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateSuggestedActions``

    Args:
        added_actions (List of :class:`telegram.api.types.SuggestedAction`):
            Added suggested actions 
        removed_actions (List of :class:`telegram.api.types.SuggestedAction`):
            Removed suggested actions

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSuggestedActions"

    def __init__(self, added_actions, removed_actions, **kwargs):
        
        self.added_actions = added_actions  # list of SuggestedAction
        self.removed_actions = removed_actions  # list of SuggestedAction

    @staticmethod
    def read(q: dict, *args) -> "UpdateSuggestedActions":
        added_actions = [Object.read(i) for i in q.get('added_actions', [])]
        removed_actions = [Object.read(i) for i in q.get('removed_actions', [])]
        return UpdateSuggestedActions(added_actions, removed_actions)
