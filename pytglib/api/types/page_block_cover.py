

from ..utils import Object


class PageBlockCover(Object):
    """
    A page cover 

    Attributes:
        ID (:obj:`str`): ``PageBlockCover``

    Args:
        cover (:class:`telegram.api.types.PageBlock`):
            Cover

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockCover"

    def __init__(self, cover, **kwargs):
        
        self.cover = cover  # PageBlock

    @staticmethod
    def read(q: dict, *args) -> "PageBlockCover":
        cover = Object.read(q.get('cover'))
        return PageBlockCover(cover)
