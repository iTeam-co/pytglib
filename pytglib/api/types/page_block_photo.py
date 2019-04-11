

from ..utils import Object


class PageBlockPhoto(Object):
    """
    A photo 

    Attributes:
        ID (:obj:`str`): ``PageBlockPhoto``

    Args:
        photo (:class:`telegram.api.types.photo`):
            Photo file; may be null 
        caption (:class:`telegram.api.types.RichText`):
            Photo caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockPhoto"

    def __init__(self, photo, caption, **kwargs):
        
        self.photo = photo  # Photo
        self.caption = caption  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockPhoto":
        photo = Object.read(q.get('photo'))
        caption = Object.read(q.get('caption'))
        return PageBlockPhoto(photo, caption)
