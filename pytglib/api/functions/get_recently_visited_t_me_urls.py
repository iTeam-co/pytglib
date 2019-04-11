

from ..utils import Object


class GetRecentlyVisitedTMeUrls(Object):
    """
    Returns t.me URLs recently visited by a newly registered user 

    Attributes:
        ID (:obj:`str`): ``GetRecentlyVisitedTMeUrls``

    Args:
        referrer (:obj:`str`):
            Google Play referrer to identify the user

    Returns:
        TMeUrls

    Raises:
        :class:`telegram.Error`
    """
    ID = "getRecentlyVisitedTMeUrls"

    def __init__(self, referrer, extra=None, **kwargs):
        self.extra = extra
        self.referrer = referrer  # str

    @staticmethod
    def read(q: dict, *args) -> "GetRecentlyVisitedTMeUrls":
        referrer = q.get('referrer')
        return GetRecentlyVisitedTMeUrls(referrer)
