

from ..utils import Object


class UserProfilePhotos(Object):
    """
    Contains part of the list of user photos 

    Attributes:
        ID (:obj:`str`): ``UserProfilePhotos``

    Args:
        total_count (:obj:`int`):
            Total number of user profile photos 
        photos (List of :class:`telegram.api.types.userProfilePhoto`):
            A list of photos

    Returns:
        UserProfilePhotos

    Raises:
        :class:`telegram.Error`
    """
    ID = "userProfilePhotos"

    def __init__(self, total_count, photos, **kwargs):
        
        self.total_count = total_count  # int
        self.photos = photos  # list of userProfilePhoto

    @staticmethod
    def read(q: dict, *args) -> "UserProfilePhotos":
        total_count = q.get('total_count')
        photos = [Object.read(i) for i in q.get('photos', [])]
        return UserProfilePhotos(total_count, photos)
