

from ..utils import Object


class Wallpaper(Object):
    """
    Contains information about a wallpaper 

    Attributes:
        ID (:obj:`str`): ``Wallpaper``

    Args:
        id (:obj:`int`):
            Unique persistent wallpaper identifier 
        sizes (List of :class:`telegram.api.types.photoSize`):
            Available variants of the wallpaper in different sizesThese photos can only be downloaded; they can't be sent in a message 
        color (:obj:`int`):
            Main color of the wallpaper in RGB24 format; should be treated as background color if no photos are specified

    Returns:
        Wallpaper

    Raises:
        :class:`telegram.Error`
    """
    ID = "wallpaper"

    def __init__(self, id, sizes, color, **kwargs):
        
        self.id = id  # int
        self.sizes = sizes  # list of photoSize
        self.color = color  # int

    @staticmethod
    def read(q: dict, *args) -> "Wallpaper":
        id = q.get('id')
        sizes = [Object.read(i) for i in q.get('sizes', [])]
        color = q.get('color')
        return Wallpaper(id, sizes, color)
