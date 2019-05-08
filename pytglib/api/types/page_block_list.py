

from ..utils import Object


class PageBlockList(Object):
    """
    A list of data blocks 

    Attributes:
        ID (:obj:`str`): ``PageBlockList``

    Args:
        items (List of :class:`telegram.api.types.pageBlockListItem`):
            The items of the list

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockList"

    def __init__(self, items, **kwargs):
        
        self.items = items  # list of pageBlockListItem

    @staticmethod
    def read(q: dict, *args) -> "PageBlockList":
        items = [Object.read(i) for i in q.get('items', [])]
        return PageBlockList(items)
