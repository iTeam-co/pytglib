

from ..utils import Object


class WebPageInstantView(Object):
    """
    Describes an instant view page for a web page

    Attributes:
        ID (:obj:`str`): ``WebPageInstantView``

    Args:
        page_blocks (List of :class:`telegram.api.types.PageBlock`):
            Content of the web page
        view_count (:obj:`int`):
            Number of the instant view views; 0 if unknown
        version (:obj:`int`):
            Version of the instant view; currently, can be 1 or 2
        is_rtl (:obj:`bool`):
            True, if the instant view must be shown from right to left
        is_full (:obj:`bool`):
            True, if the instant view contains the full pageA network request might be needed to get the full web page instant view
        feedback_link (:class:`telegram.api.types.InternalLinkType`):
            An internal link to be opened to leave feedback about the instant view

    Returns:
        WebPageInstantView

    Raises:
        :class:`telegram.Error`
    """
    ID = "webPageInstantView"

    def __init__(self, page_blocks, view_count, version, is_rtl, is_full, feedback_link, **kwargs):
        
        self.page_blocks = page_blocks  # list of PageBlock
        self.view_count = view_count  # int
        self.version = version  # int
        self.is_rtl = is_rtl  # bool
        self.is_full = is_full  # bool
        self.feedback_link = feedback_link  # InternalLinkType

    @staticmethod
    def read(q: dict, *args) -> "WebPageInstantView":
        page_blocks = [Object.read(i) for i in q.get('page_blocks', [])]
        view_count = q.get('view_count')
        version = q.get('version')
        is_rtl = q.get('is_rtl')
        is_full = q.get('is_full')
        feedback_link = Object.read(q.get('feedback_link'))
        return WebPageInstantView(page_blocks, view_count, version, is_rtl, is_full, feedback_link)
