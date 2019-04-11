

from ..utils import Object


class ViewTrendingStickerSets(Object):
    """
    Informs the server that some trending sticker sets have been viewed by the user 

    Attributes:
        ID (:obj:`str`): ``ViewTrendingStickerSets``

    Args:
        sticker_set_ids (List of :obj:`int`):
            Identifiers of viewed trending sticker sets

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "viewTrendingStickerSets"

    def __init__(self, sticker_set_ids, extra=None, **kwargs):
        self.extra = extra
        self.sticker_set_ids = sticker_set_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "ViewTrendingStickerSets":
        sticker_set_ids = q.get('sticker_set_ids')
        return ViewTrendingStickerSets(sticker_set_ids)
