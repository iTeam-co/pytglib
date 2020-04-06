

from ..utils import Object


class GetUserProfilePhotos(Object):
    """
    Returns the profile photos of a user. The result of this query may be outdated: some photos might have been deleted already 

    Attributes:
        ID (:obj:`str`): ``GetUserProfilePhotos``

    Args:
        user_id (:obj:`int`):
            User identifier 
        offset (:obj:`int`):
            The number of photos to skip; must be non-negative 
        limit (:obj:`int`):
            The maximum number of photos to be returned; up to 100

    Returns:
        UserProfilePhotos

    Raises:
        :class:`telegram.Error`
    """
    ID = "getUserProfilePhotos"

    def __init__(self, user_id, offset, limit, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(q: dict, *args) -> "GetUserProfilePhotos":
        user_id = q.get('user_id')
        offset = q.get('offset')
        limit = q.get('limit')
        return GetUserProfilePhotos(user_id, offset, limit)
