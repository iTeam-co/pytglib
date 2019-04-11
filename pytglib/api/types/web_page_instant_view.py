

from ..utils import Object


class WebPageInstantView(Object):
    """
    Describes an instant view page for a web page 

    Attributes:
        ID (:obj:`str`): ``WebPageInstantView``

    Args:
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Content of the web page 
        is_full (:obj:`bool`):
            True, if the instant view contains the full pageA network request might be needed to get the full web page instant view

    Returns:
        WebPageInstantView

    Raises:
        :class:`telegram.Error`
    """
    ID = "webPageInstantView"

    def __init__(self, page_blocks, is_full, **kwargs):
        
        self.page_blocks = page_blocks  # list of PageBlock
        self.is_full = is_full  # bool

    @staticmethod
    def read(q: dict, *args) -> "WebPageInstantView":
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        is_full = q.get('is_full')
        return WebPageInstantView(page_blocks, is_full)
