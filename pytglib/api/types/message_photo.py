

from ..utils import Object


class MessagePhoto(Object):
    """
    A photo message 

    Attributes:
        ID (:obj:`str`): ``MessagePhoto``

    Args:
        photo (:class:`telegram.api.types.photo`):
            The photo description 
        caption (:class:`telegram.api.types.formattedText`):
            Photo caption 
        is_secret (:obj:`bool`):
            True, if the photo must be blurred and must be shown only while tapped

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messagePhoto"

    def __init__(self, photo, caption, is_secret, **kwargs):
        
        self.photo = photo  # Photo
        self.caption = caption  # FormattedText
        self.is_secret = is_secret  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessagePhoto":
        photo = Object.read(q.get('photo'))
        caption = Object.read(q.get('caption'))
        is_secret = q.get('is_secret')
        return MessagePhoto(photo, caption, is_secret)
