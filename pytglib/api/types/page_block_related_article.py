

from ..utils import Object


class PageBlockRelatedArticle(Object):
    """
    Contains information about a related article 

    Attributes:
        ID (:obj:`str`): ``PageBlockRelatedArticle``

    Args:
        url (:obj:`str`):
            Related article URL 
        title (:obj:`str`):
            Article title; may be empty 
        description (:obj:`str`):
            Article description; may be empty
        photo (:class:`telegram.api.types.photo`):
            Article photo; may be null 
        author (:obj:`str`):
            Article author; may be empty 
        publish_date (:obj:`int`):
            Point in time (Unix timestamp) when the article was published; 0 if unknown

    Returns:
        PageBlockRelatedArticle

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockRelatedArticle"

    def __init__(self, url, title, description, photo, author, publish_date, **kwargs):
        
        self.url = url  # str
        self.title = title  # str
        self.description = description  # str
        self.photo = photo  # Photo
        self.author = author  # str
        self.publish_date = publish_date  # int

    @staticmethod
    def read(q: dict, *args) -> "PageBlockRelatedArticle":
        url = q.get('url')
        title = q.get('title')
        description = q.get('description')
        photo = Object.read(q.get('photo'))
        author = q.get('author')
        publish_date = q.get('publish_date')
        return PageBlockRelatedArticle(url, title, description, photo, author, publish_date)
