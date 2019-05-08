

from ..utils import Object


class PageBlockTable(Object):
    """
    A table 

    Attributes:
        ID (:obj:`str`): ``PageBlockTable``

    Args:
        caption (:class:`telegram.api.types.RichText`):
            Table caption 
        cells (List of List of :class:`telegram.api.types.pageBlockTableCell`):
            Table cells 
        is_bordered (:obj:`bool`):
            True, if the table is bordered 
        is_striped (:obj:`bool`):
            True, if the table is striped

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockTable"

    def __init__(self, caption, cells, is_bordered, is_striped, **kwargs):
        
        self.caption = caption  # RichText
        self.cells = cells  # list of list(pageBlockTableCell)
        self.is_bordered = is_bordered  # bool
        self.is_striped = is_striped  # bool

    @staticmethod
    def read(q: dict, *args) -> "PageBlockTable":
        caption = Object.read(q.get('caption'))
        cells = [[Object.read(v) for v in i] for i in q.get('cells', [])]
        is_bordered = q.get('is_bordered')
        is_striped = q.get('is_striped')
        return PageBlockTable(caption, cells, is_bordered, is_striped)
