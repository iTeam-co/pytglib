

from ..utils import Object


class Photo(Object):
    """
    Describes a photo 

    Attributes:
        ID (:obj:`str`): ``Photo``

    Args:
        has_stickers (:obj:`bool`):
            True, if stickers were added to the photo 
        minithumbnail (:class:`telegram.api.types.minithumbnail`):
            Photo minithumbnail; may be null 
        sizes (List of :class:`telegram.api.types.photoSize`):
            Available variants of the photo, in different sizes

    Returns:
        Photo

    Raises:
        :class:`telegram.Error`
    """
    ID = "photo"

    def __init__(self, has_stickers, minithumbnail, sizes, **kwargs):
        
        self.has_stickers = has_stickers  # bool
        self.minithumbnail = minithumbnail  # Minithumbnail
        self.sizes = sizes  # list of photoSize

    @staticmethod
    def read(q: dict, *args) -> "Photo":
        has_stickers = q.get('has_stickers')
        minithumbnail = Object.read(q.get('minithumbnail'))
        sizes = [Object.read(i) for i in q.get('sizes', [])]
        return Photo(has_stickers, minithumbnail, sizes)
