

from ..utils import Object


class UpdateSavedAnimations(Object):
    """
    The list of saved animations was updated 

    Attributes:
        ID (:obj:`str`): ``UpdateSavedAnimations``

    Args:
        animation_ids (List of :obj:`int`):
            The new list of file identifiers of saved animations

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateSavedAnimations"

    def __init__(self, animation_ids, **kwargs):
        
        self.animation_ids = animation_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "UpdateSavedAnimations":
        animation_ids = q.get('animation_ids')
        return UpdateSavedAnimations(animation_ids)
