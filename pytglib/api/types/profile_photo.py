

from ..utils import Object


class ProfilePhoto(Object):
    """
    Describes a user profile photo 

    Attributes:
        ID (:obj:`str`): ``ProfilePhoto``

    Args:
        id (:obj:`int`):
            Photo identifier; 0 for an empty photoCan be used to find a photo in a list of userProfilePhotos
        small (:class:`telegram.api.types.file`):
            A small (160x160) user profile photoThe file can be downloaded only before the photo is changed 
        big (:class:`telegram.api.types.file`):
            A big (640x640) user profile photoThe file can be downloaded only before the photo is changed

    Returns:
        ProfilePhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "profilePhoto"

    def __init__(self, id, small, big, **kwargs):
        
        self.id = id  # int
        self.small = small  # File
        self.big = big  # File

    @staticmethod
    def read(q: dict, *args) -> "ProfilePhoto":
        id = q.get('id')
        small = Object.read(q.get('small'))
        big = Object.read(q.get('big'))
        return ProfilePhoto(id, small, big)
