

from ..utils import Object


class InlineQueryResultAnimation(Object):
    """
    Represents an animation file 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultAnimation``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        animation (:class:`telegram.api.types.animation`):
            Animation file 
        title (:obj:`str`):
            Animation title

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultAnimation"

    def __init__(self, id, animation, title, **kwargs):
        
        self.id = id  # str
        self.animation = animation  # Animation
        self.title = title  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultAnimation":
        id = q.get('id')
        animation = Object.read(q.get('animation'))
        title = q.get('title')
        return InlineQueryResultAnimation(id, animation, title)
