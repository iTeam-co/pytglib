

from ..utils import Object


class Hashtags(Object):
    """
    Contains a list of hashtags 

    Attributes:
        ID (:obj:`str`): ``Hashtags``

    Args:
        hashtags (List of :obj:`str`):
            A list of hashtags

    Returns:
        Hashtags

    Raises:
        :class:`telegram.Error`
    """
    ID = "hashtags"

    def __init__(self, hashtags, **kwargs):
        
        self.hashtags = hashtags  # list of str

    @staticmethod
    def read(q: dict, *args) -> "Hashtags":
        hashtags = q.get('hashtags')
        return Hashtags(hashtags)
