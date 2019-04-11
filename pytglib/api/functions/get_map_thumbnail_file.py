

from ..utils import Object


class GetMapThumbnailFile(Object):
    """
    Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded 

    Attributes:
        ID (:obj:`str`): ``GetMapThumbnailFile``

    Args:
        location (:class:`telegram.api.types.location`):
            Location of the map center 
        zoom (:obj:`int`):
            Map zoom level; 13-20 
        width (:obj:`int`):
            Map width in pixels before applying scale; 16-1024 
        height (:obj:`int`):
            Map height in pixels before applying scale; 16-1024 
        scale (:obj:`int`):
            Map scale; 1-3 
        chat_id (:obj:`int`):
            Identifier of a chat, in which the thumbnail will be shownUse 0 if unknown

    Returns:
        File

    Raises:
        :class:`telegram.Error`
    """
    ID = "getMapThumbnailFile"

    def __init__(self, location, zoom, width, height, scale, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.location = location  # Location
        self.zoom = zoom  # int
        self.width = width  # int
        self.height = height  # int
        self.scale = scale  # int
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetMapThumbnailFile":
        location = Object.read(q.get('location'))
        zoom = q.get('zoom')
        width = q.get('width')
        height = q.get('height')
        scale = q.get('scale')
        chat_id = q.get('chat_id')
        return GetMapThumbnailFile(location, zoom, width, height, scale, chat_id)
