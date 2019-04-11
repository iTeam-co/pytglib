

from ..utils import Object


class LinkState(Object):
    """
    Represents the relationship between user A and user B. For incoming_link, user A is the current user; for outgoing_link, user B is the current user

    No parameters required.
    """
    ID = "linkState"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LinkStateKnowsPhoneNumber or LinkStateIsContact or LinkStateNone":
        if q.get("@type"):
            return Object.read(q)
        return LinkState()
