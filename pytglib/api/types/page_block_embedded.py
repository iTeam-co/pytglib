

from ..utils import Object


class PageBlockEmbedded(Object):
    """
    An embedded web page 

    Attributes:
        ID (:obj:`str`): ``PageBlockEmbedded``

    Args:
        url (:obj:`str`):
            Web page URL, if available 
        html (:obj:`str`):
            HTML-markup of the embedded page 
        poster_photo (:class:`telegram.api.types.photo`):
            Poster photo, if available; may be null 
        width (:obj:`int`):
            Block width; 0 if unknown 
        height (:obj:`int`):
            Block height; 0 if unknown 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Block caption 
        is_full_width (:obj:`bool`):
            True, if the block should be full width 
        allow_scrolling (:obj:`bool`):
            True, if scrolling should be allowed

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockEmbedded"

    def __init__(self, url, html, poster_photo, width, height, caption, is_full_width, allow_scrolling, **kwargs):
        
        self.url = url  # str
        self.html = html  # str
        self.poster_photo = poster_photo  # Photo
        self.width = width  # int
        self.height = height  # int
        self.caption = caption  # PageBlockCaption
        self.is_full_width = is_full_width  # bool
        self.allow_scrolling = allow_scrolling  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockEmbedded":
        url = q.get('url')
        html = q.get('html')
        poster_photo = Object.read(q.get('poster_photo'))
        width = q.get('width')
        height = q.get('height')
        caption = Object.read(q.get('caption'))
        is_full_width = q.get('is_full_width')
        allow_scrolling = q.get('allow_scrolling')
        return PageBlockEmbedded(url, html, poster_photo, width, height, caption, is_full_width, allow_scrolling)
