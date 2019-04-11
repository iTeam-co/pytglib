

from ..utils import Object


class RemoveSavedAnimation(Object):
    """
    Removes an animation from the list of saved animations 

    Attributes:
        ID (:obj:`str`): ``RemoveSavedAnimation``

    Args:
        animation (:class:`telegram.api.types.InputFile`):
            Animation file to be removed

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeSavedAnimation"

    def __init__(self, animation, extra=None, **kwargs):
        self.extra = extra
        self.animation = animation  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "RemoveSavedAnimation":
        animation = Object.read(q.get('animation'))
        return RemoveSavedAnimation(animation)
