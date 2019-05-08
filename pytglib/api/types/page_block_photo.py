

from ..utils import Object


class PageBlockPhoto(Object):
    """
    A photo 

    Attributes:
        ID (:obj:`str`): ``PageBlockPhoto``

    Args:
        photo (:class:`telegram.api.types.photo`):
            Photo file; may be null 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Photo caption 
        url (:obj:`str`):
            URL that needs to be opened when the photo is clicked

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockPhoto"

    def __init__(self, photo, caption, url, **kwargs):
        
        self.photo = photo  # Photo
        self.caption = caption  # PageBlockCaption
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "PageBlockPhoto":
        photo = Object.read(q.get('photo'))
        caption = Object.read(q.get('caption'))
        url = q.get('url')
        return PageBlockPhoto(photo, caption, url)
