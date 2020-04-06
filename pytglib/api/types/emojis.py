

from ..utils import Object


class Emojis(Object):
    """
    Represents a list of emoji 

    Attributes:
        ID (:obj:`str`): ``Emojis``

    Args:
        emojis (List of :obj:`str`):
            List of emojis

    Returns:
        Emojis

    Raises:
        :class:`telegram.Error`
    """
    ID = "emojis"

    def __init__(self, emojis, **kwargs):
        
        self.emojis = emojis  # list of str

    @staticmethod
    def read(q: dict, *args) -> "Emojis":
        emojis = q.get('emojis')
        return Emojis(emojis)
