

from ..utils import Object


class PageBlockTableCell(Object):
    """
    Represents a cell of a table 

    Attributes:
        ID (:obj:`str`): ``PageBlockTableCell``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Cell text; may be nullIf the text is null, then the cell should be invisible 
        is_header (:obj:`bool`):
            True, if it is a header cell
        colspan (:obj:`int`):
            The number of columns the cell should span 
        rowspan (:obj:`int`):
            The number of rows the cell should span
        align (:class:`telegram.api.types.PageBlockHorizontalAlignment`):
            Horizontal cell content alignment 
        valign (:class:`telegram.api.types.PageBlockVerticalAlignment`):
            Vertical cell content alignment

    Returns:
        PageBlockTableCell

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockTableCell"

    def __init__(self, text, is_header, colspan, rowspan, align, valign, **kwargs):
        
        self.text = text  # RichText
        self.is_header = is_header  # bool
        self.colspan = colspan  # int
        self.rowspan = rowspan  # int
        self.align = align  # PageBlockHorizontalAlignment
        self.valign = valign  # PageBlockVerticalAlignment

    @staticmethod
    def read(q: dict, *args) -> "PageBlockTableCell":
        text = Object.read(q.get('text'))
        is_header = q.get('is_header')
        colspan = q.get('colspan')
        rowspan = q.get('rowspan')
        align = Object.read(q.get('align'))
        valign = Object.read(q.get('valign'))
        return PageBlockTableCell(text, is_header, colspan, rowspan, align, valign)
