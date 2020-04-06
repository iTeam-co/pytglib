

from ..utils import Object


class ChatEventPhotoChanged(Object):
    """
    The chat photo was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventPhotoChanged``

    Args:
        old_photo (:class:`telegram.api.types.photo`):
            Previous chat photo value; may be null 
        new_photo (:class:`telegram.api.types.photo`):
            New chat photo value; may be null

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventPhotoChanged"

    def __init__(self, old_photo, new_photo, **kwargs):
        
        self.old_photo = old_photo  # Photo
        self.new_photo = new_photo  # Photo

    @staticmethod
    def read(q: dict, *args) -> "ChatEventPhotoChanged":
        old_photo = Object.read(q.get('old_photo'))
        new_photo = Object.read(q.get('new_photo'))
        return ChatEventPhotoChanged(old_photo, new_photo)
