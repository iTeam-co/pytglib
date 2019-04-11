

from ..utils import Object


class InlineQueryResultPhoto(Object):
    """
    Represents a photo 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultPhoto``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        photo (:class:`telegram.api.types.photo`):
            Photo 
        title (:obj:`str`):
            Title of the result, if known 
        description (:obj:`str`):
            A short description of the result, if known

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultPhoto"

    def __init__(self, id, photo, title, description, **kwargs):
        
        self.id = id  # str
        self.photo = photo  # Photo
        self.title = title  # str
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultPhoto":
        id = q.get('id')
        photo = Object.read(q.get('photo'))
        title = q.get('title')
        description = q.get('description')
        return InlineQueryResultPhoto(id, photo, title, description)
