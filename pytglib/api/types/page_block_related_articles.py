

from ..utils import Object


class PageBlockRelatedArticles(Object):
    """
    Related articles 

    Attributes:
        ID (:obj:`str`): ``PageBlockRelatedArticles``

    Args:
        header (:class:`telegram.api.types.RichText`):
            Block header 
        articles (List of :class:`telegram.api.types.pageBlockRelatedArticle`):
            List of related articles

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockRelatedArticles"

    def __init__(self, header, articles, **kwargs):
        
        self.header = header  # RichText
        self.articles = articles  # list of pageBlockRelatedArticle

    @staticmethod
    def read(q: dict, *args) -> "PageBlockRelatedArticles":
        header = Object.read(q.get('header'))
        articles = [Object.read(i) for i in q.get('articles', [])]
        return PageBlockRelatedArticles(header, articles)
