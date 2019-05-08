

from ..utils import Object


class PushMessageContentPhoto(Object):
    """
    A photo message 

    Attributes:
        ID (:obj:`str`): ``PushMessageContentPhoto``

    Args:
        photo (:class:`telegram.api.types.photo`):
            Message content; may be null 
        caption (:obj:`str`):
            Photo caption 
        is_secret (:obj:`bool`):
            True, if the photo is secret 
        is_pinned (:obj:`bool`):
            True, if the message is a pinned message with the specified content

    Returns:
        PushMessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "pushMessageContentPhoto"

    def __init__(self, photo, caption, is_secret, is_pinned, **kwargs):
        
        self.photo = photo  # Photo
        self.caption = caption  # str
        self.is_secret = is_secret  # bool
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "PushMessageContentPhoto":
        photo = Object.read(q.get('photo'))
        caption = q.get('caption')
        is_secret = q.get('is_secret')
        is_pinned = q.get('is_pinned')
        return PushMessageContentPhoto(photo, caption, is_secret, is_pinned)
