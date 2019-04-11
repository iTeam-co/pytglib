

from ..utils import Object


class RemoveRecentHashtag(Object):
    """
    Removes a hashtag from the list of recently used hashtags 

    Attributes:
        ID (:obj:`str`): ``RemoveRecentHashtag``

    Args:
        hashtag (:obj:`str`):
            Hashtag to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "removeRecentHashtag"

    def __init__(self, hashtag, extra=None, **kwargs):
        self.extra = extra
        self.hashtag = hashtag  # str

    @staticmethod
    def read(q: dict, *args) -> "RemoveRecentHashtag":
        hashtag = q.get('hashtag')
        return RemoveRecentHashtag(hashtag)
