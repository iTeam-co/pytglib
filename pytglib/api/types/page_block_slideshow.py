

from ..utils import Object


class PageBlockSlideshow(Object):
    """
    A slideshow 

    Attributes:
        ID (:obj:`str`): ``PageBlockSlideshow``

    Args:
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Slideshow item contents 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Block caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockSlideshow"

    def __init__(self, page_blocks, caption, **kwargs):
        
        self.page_blocks = page_blocks  # list of PageBlock
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockSlideshow":
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        caption = Object.read(q.get('caption'))
        return PageBlockSlideshow(page_blocks, caption)
