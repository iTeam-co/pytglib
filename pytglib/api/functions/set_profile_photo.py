

from ..utils import Object


class SetProfilePhoto(Object):
    """
    Uploads a new profile photo for the current user. If something changes, updateUser will be sent 

    Attributes:
        ID (:obj:`str`): ``SetProfilePhoto``

    Args:
        photo (:class:`telegram.api.types.InputFile`):
            Profile photo to setinputFileId and inputFileRemote may still be unsupported

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setProfilePhoto"

    def __init__(self, photo, extra=None, **kwargs):
        self.extra = extra
        self.photo = photo  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "SetProfilePhoto":
        photo = Object.read(q.get('photo'))
        return SetProfilePhoto(photo)
