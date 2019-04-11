

from ..utils import Object


class InlineQueryResultVideo(Object):
    """
    Represents a video 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultVideo``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        video (:class:`telegram.api.types.video`):
            Video 
        title (:obj:`str`):
            Title of the video 
        description (:obj:`str`):
            Description of the video

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultVideo"

    def __init__(self, id, video, title, description, **kwargs):
        
        self.id = id  # str
        self.video = video  # Video
        self.title = title  # str
        self.description = description  # str

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultVideo":
        id = q.get('id')
        video = Object.read(q.get('video'))
        title = q.get('title')
        description = q.get('description')
        return InlineQueryResultVideo(id, video, title, description)
