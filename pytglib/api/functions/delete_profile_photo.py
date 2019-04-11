

from ..utils import Object


class DeleteProfilePhoto(Object):
    """
    Deletes a profile photo. If something changes, updateUser will be sent 

    Attributes:
        ID (:obj:`str`): ``DeleteProfilePhoto``

    Args:
        profile_photo_id (:obj:`int`):
            Identifier of the profile photo to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteProfilePhoto"

    def __init__(self, profile_photo_id, extra=None, **kwargs):
        self.extra = extra
        self.profile_photo_id = profile_photo_id  # int

    @staticmethod
    def read(q: dict, *args) -> "DeleteProfilePhoto":
        profile_photo_id = q.get('profile_photo_id')
        return DeleteProfilePhoto(profile_photo_id)
