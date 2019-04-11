

from ..utils import Object


class InlineQueryResultArticle(Object):
    """
    Represents a link to an article or web page 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultArticle``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        url (:obj:`str`):
            URL of the result, if it exists 
        hide_url (:obj:`bool`):
            True, if the URL must be not shown 
        title (:obj:`str`):
            Title of the result
        description (:obj:`str`):
            A short description of the result 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Result thumbnail; may be null

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultArticle"

    def __init__(self, id, url, hide_url, title, description, thumbnail, **kwargs):
        
        self.id = id  # str
        self.url = url  # str
        self.hide_url = hide_url  # bool
        self.title = title  # str
        self.description = description  # str
        self.thumbnail = thumbnail  # PhotoSize

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultArticle":
        id = q.get('id')
        url = q.get('url')
        hide_url = q.get('hide_url')
        title = q.get('title')
        description = q.get('description')
        thumbnail = Object.read(q.get('thumbnail'))
        return InlineQueryResultArticle(id, url, hide_url, title, description, thumbnail)
