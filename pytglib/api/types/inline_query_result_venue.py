

from ..utils import Object


class InlineQueryResultVenue(Object):
    """
    Represents information about a venue 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultVenue``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        venue (:class:`telegram.api.types.venue`):
            Venue result 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Result thumbnail; may be null

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultVenue"

    def __init__(self, id, venue, thumbnail, **kwargs):
        
        self.id = id  # str
        self.venue = venue  # Venue
        self.thumbnail = thumbnail  # PhotoSize

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultVenue":
        id = q.get('id')
        venue = Object.read(q.get('venue'))
        thumbnail = Object.read(q.get('thumbnail'))
        return InlineQueryResultVenue(id, venue, thumbnail)
