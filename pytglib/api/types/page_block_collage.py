

from ..utils import Object


class PageBlockCollage(Object):
    """
    A collage 

    Attributes:
        ID (:obj:`str`): ``PageBlockCollage``

    Args:
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Collage item contents 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Block caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockCollage"

    def __init__(self, page_blocks, caption, **kwargs):
        
        self.page_blocks = page_blocks  # list of PageBlock
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockCollage":
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        caption = Object.read(q.get('caption'))
        return PageBlockCollage(page_blocks, caption)
