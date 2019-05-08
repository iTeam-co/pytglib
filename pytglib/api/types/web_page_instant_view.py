

from ..utils import Object


class WebPageInstantView(Object):
    """
    Describes an instant view page for a web page 

    Attributes:
        ID (:obj:`str`): ``WebPageInstantView``

    Args:
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Content of the web page
        version (:obj:`int`):
            Version of the instant view, currently can be 1 or 2
        url (:obj:`str`):
            Instant view URL; may be different from WebPageurl and must be used for the correct anchors handling
        is_rtl (:obj:`bool`):
            True, if the instant view must be shown from right to left
        is_full (:obj:`bool`):
            True, if the instant view contains the full pageA network request might be needed to get the full web page instant view

    Returns:
        WebPageInstantView

    Raises:
        :class:`telegram.Error`
    """
    ID = "webPageInstantView"

    def __init__(self, page_blocks, version, url, is_rtl, is_full, **kwargs):
        
        self.page_blocks = page_blocks  # list of PageBlock
        self.version = version  # int
        self.url = url  # str
        self.is_rtl = is_rtl  # bool
        self.is_full = is_full  # bool

    @staticmethod
    def read(q: dict, *args) -> "WebPageInstantView":
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        version = q.get('version')
        url = q.get('url')
        is_rtl = q.get('is_rtl')
        is_full = q.get('is_full')
        return WebPageInstantView(page_blocks, version, url, is_rtl, is_full)
