

from ..utils import Object


class PageBlockDetails(Object):
    """
    A collapsible block 

    Attributes:
        ID (:obj:`str`): ``PageBlockDetails``

    Args:
        header (:class:`telegram.api.types.RichText`):
            Always visible heading for the block 
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Block contents 
        is_open (:obj:`bool`):
            True, if the block is open by default

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockDetails"

    def __init__(self, header, page_blocks, is_open, **kwargs):
        
        self.header = header  # RichText
        self.page_blocks = page_blocks  # list of PageBlock
        self.is_open = is_open  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockDetails":
        header = Object.read(q.get('header'))
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        is_open = q.get('is_open')
        return PageBlockDetails(header, page_blocks, is_open)
