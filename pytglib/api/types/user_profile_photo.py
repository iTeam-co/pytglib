

from ..utils import Object


class UserProfilePhoto(Object):
    """
    Contains full information about a user profile photo 

    Attributes:
        ID (:obj:`str`): ``UserProfilePhoto``

    Args:
        id (:obj:`int`):
            Unique user profile photo identifier 
        added_date (:obj:`int`):
            Point in time (Unix timestamp) when the photo has been added 
        sizes (List of :class:`telegram.api.types.photoSize`):
            Available variants of the user photo, in different sizes

    Returns:
        UserProfilePhoto

    Raises:
        :class:`telegram.Error`
    """
    ID = "userProfilePhoto"

    def __init__(self, id, added_date, sizes, **kwargs):
        
        self.id = id  # int
        self.added_date = added_date  # int
        self.sizes = sizes  # list of photoSize

    @staticmethod
    def read(q: dict, *args) -> "UserProfilePhoto":
        id = q.get('id')
        added_date = q.get('added_date')
        sizes = [Object.read(i) for i in q.get('sizes', [])]
        return UserProfilePhoto(id, added_date, sizes)
