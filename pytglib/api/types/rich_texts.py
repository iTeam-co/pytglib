

from ..utils import Object


class RichTexts(Object):
    """
    A concatenation of rich texts 

    Attributes:
        ID (:obj:`str`): ``RichTexts``

    Args:
        texts (List of :class:`telegram.api.types.RichText`):
            Texts

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTexts"

    def __init__(self, texts, **kwargs):
        
        self.texts = texts  # list of RichText

    @staticmethod
    def read(q: dict, *args) -> "RichTexts":
        texts = [Object.read(i) for i in q.get('texts', [])]
        return RichTexts(texts)
