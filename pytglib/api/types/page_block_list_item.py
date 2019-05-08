

from ..utils import Object


class PageBlockListItem(Object):
    """
    Describes an item of a list page block 

    Attributes:
        ID (:obj:`str`): ``PageBlockListItem``

    Args:
        label (:obj:`str`):
            Item label 
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Item blocks

    Returns:
        PageBlockListItem

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockListItem"

    def __init__(self, label, page_blocks, **kwargs):
        
        self.label = label  # str
        self.page_blocks = page_blocks  # list of PageBlock

    @staticmethod
    def read(q: dict, *args) -> "PageBlockListItem":
        label = q.get('label')
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        return PageBlockListItem(label, page_blocks)
