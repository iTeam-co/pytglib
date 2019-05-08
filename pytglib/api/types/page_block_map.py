

from ..utils import Object


class PageBlockMap(Object):
    """
    A map 

    Attributes:
        ID (:obj:`str`): ``PageBlockMap``

    Args:
        location (:class:`telegram.api.types.location`):
            Location of the map center 
        zoom (:obj:`int`):
            Map zoom level 
        width (:obj:`int`):
            Map width 
        height (:obj:`int`):
            Map height 
        caption (:class:`telegram.api.types.pageBlockCaption`):
            Block caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockMap"

    def __init__(self, location, zoom, width, height, caption, **kwargs):
        
        self.location = location  # Location
        self.zoom = zoom  # int
        self.width = width  # int
        self.height = height  # int
        self.caption = caption  # PageBlockCaption

    @staticmethod
    def read(q: dict, *args) -> "PageBlockMap":
        location = Object.read(q.get('location'))
        zoom = q.get('zoom')
        width = q.get('width')
        height = q.get('height')
        caption = Object.read(q.get('caption'))
        return PageBlockMap(location, zoom, width, height, caption)
