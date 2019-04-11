

from ..utils import Object


class InlineQueryResultLocation(Object):
    """
    Represents a point on the map 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultLocation``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        location (:class:`telegram.api.types.location`):
            Location result 
        title (:obj:`str`):
            Title of the result 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Result thumbnail; may be null

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultLocation"

    def __init__(self, id, location, title, thumbnail, **kwargs):
        
        self.id = id  # str
        self.location = location  # Location
        self.title = title  # str
        self.thumbnail = thumbnail  # PhotoSize

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultLocation":
        id = q.get('id')
        location = Object.read(q.get('location'))
        title = q.get('title')
        thumbnail = Object.read(q.get('thumbnail'))
        return InlineQueryResultLocation(id, location, title, thumbnail)
