

from ..utils import Object


class PageBlockList(Object):
    """
    A list of texts 

    Attributes:
        ID (:obj:`str`): ``PageBlockList``

    Args:
        items (List of :class:`telegram.api.types.RichText`):
            Texts 
        is_ordered (:obj:`bool`):
            True, if the items should be marked with numbers

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockList"

    def __init__(self, items, is_ordered, **kwargs):
        
        self.items = items  # list of RichText
        self.is_ordered = is_ordered  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockList":
        items = [Object.read(i) for i in q.get('items', [])]
        is_ordered = q.get('is_ordered')
        return PageBlockList(items, is_ordered)
