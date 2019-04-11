

from ..utils import Object


class PageBlockAuthorDate(Object):
    """
    The author and publishing date of a page 

    Attributes:
        ID (:obj:`str`): ``PageBlockAuthorDate``

    Args:
        author (:class:`telegram.api.types.RichText`):
            Author 
        publish_date (:obj:`int`):
            Point in time (Unix timestamp) when the article was published; 0 if unknown

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockAuthorDate"

    def __init__(self, author, publish_date, **kwargs):
        
        self.author = author  # RichText
        self.publish_date = publish_date  # int

    @staticmethod
    def read(q: dict, *args) -> "PageBlockAuthorDate":
        author = Object.read(q.get('author'))
        publish_date = q.get('publish_date')
        return PageBlockAuthorDate(author, publish_date)
