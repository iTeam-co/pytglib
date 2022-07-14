

from ..utils import Object


class SetProfilePhoto(Object):
    """
    Changes a profile photo for the current user 

    Attributes:
        ID (:obj:`str`): ``SetProfilePhoto``

    Args:
        photo (:class:`telegram.api.types.InputChatPhoto`):
            Profile photo to set

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setProfilePhoto"

    def __init__(self, photo, extra=None, **kwargs):
        self.extra = extra
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(q: dict, *args) -> "SetProfilePhoto":
        photo = Object.read(q.get('photo'))
        return SetProfilePhoto(photo)
