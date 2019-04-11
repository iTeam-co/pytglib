

from ..utils import Object


class AddSavedAnimation(Object):
    """
    Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list

    Attributes:
        ID (:obj:`str`): ``AddSavedAnimation``

    Args:
        animation (:class:`telegram.api.types.InputFile`):
            The animation file to be addedOnly animations known to the server (iesuccessfully sent via a message) can be added to the list

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "addSavedAnimation"

    def __init__(self, animation, extra=None, **kwargs):
        self.extra = extra
        self.animation = animation  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "AddSavedAnimation":
        animation = Object.read(q.get('animation'))
        return AddSavedAnimation(animation)
