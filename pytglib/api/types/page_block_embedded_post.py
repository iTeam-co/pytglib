

from ..utils import Object


class PageBlockEmbeddedPost(Object):
    """
    An embedded post 

    Attributes:
        ID (:obj:`str`): ``PageBlockEmbeddedPost``

    Args:
        url (:obj:`str`):
            Web page URL 
        author (:obj:`str`):
            Post author 
        author_photo (:class:`telegram.api.types.photo`):
            Post author photo; may be null 
        date (:obj:`int`):
            Point in time (Unix timestamp) when the post was created; 0 if unknown 
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Post content 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Post caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockEmbeddedPost"

    def __init__(self, url, author, author_photo, date, page_blocks, caption, **kwargs):
        
        self.url = url  # str
        self.author = author  # str
        self.author_photo = author_photo  # Photo
        self.date = date  # int
        self.page_blocks = page_blocks  # list of PageBlock
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockEmbeddedPost":
        url = q.get('url')
        author = q.get('author')
        author_photo = Object.read(q.get('author_photo'))
        date = q.get('date')
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        caption = Object.read(q.get('caption'))
        return PageBlockEmbeddedPost(url, author, author_photo, date, page_blocks, caption)
