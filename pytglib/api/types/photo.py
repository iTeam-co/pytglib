

from ..utils import Object


class Photo(Object):
    """
    Describes a photo 

    Attributes:
        ID (:obj:`str`): ``Photo``

    Args:
        id (:obj:`int`):
            Photo identifier; 0 for deleted photos 
        has_stickers (:obj:`bool`):
            True, if stickers were added to the photo 
        sizes (List of :class:`telegram.api.types.photoSize`):
            Available variants of the photo, in different sizes

    Returns:
        Photo

    Raises:
        :class:`telegram.Error`
    """
    ID = "photo"

    def __init__(self, id, has_stickers, sizes, **kwargs):
        
        self.id = id  # int
        self.has_stickers = has_stickers  # bool
        self.sizes = sizes  # list of photoSize

    @staticmethod
    def read(q: dict, *args) -> "Photo":
        id = q.get('id')
        has_stickers = q.get('has_stickers')
        sizes = [Object.read(i) for i in q.get('sizes', [])]
        return Photo(id, has_stickers, sizes)
