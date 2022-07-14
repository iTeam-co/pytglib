

from ..utils import Object


class ChatStatistics(Object):
    """
    Contains a detailed statistics about a chat

    No parameters required.
    """
    ID = "chatStatistics"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatStatisticsChannel or ChatStatisticsSupergroup":
        if q.get("@type"):
            return Object.read(q)
        return ChatStatistics()
