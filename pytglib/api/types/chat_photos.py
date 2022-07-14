

from ..utils import Object


class ChatPhotos(Object):
    """
    Contains a list of chat or user profile photos 

    Attributes:
        ID (:obj:`str`): ``ChatPhotos``

    Args:
        total_count (:obj:`int`):
            Total number of photos 
        photos (List of :class:`telegram.api.types.chatPhoto`):
            List of photos

    Returns:
        ChatPhotos

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPhotos"

    def __init__(self, total_count, photos, **kwargs):
        
        self.total_count = total_count  # int
        self.photos = photos  # list of chatPhoto

    @staticmethod
    def read(q: dict, *args) -> "ChatPhotos":
        total_count = q.get('total_count')
        photos = [Object.read(i) for i in q.get('photos', [])]
        return ChatPhotos(total_count, photos)
