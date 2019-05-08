

from ..utils import Object


class TopChatCategory(Object):
    """
    Represents the categories of chats for which a list of frequently used chats can be retrieved

    No parameters required.
    """
    ID = "topChatCategory"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "TopChatCategoryUsers or TopChatCategoryChannels or TopChatCategoryGroups or TopChatCategoryCalls or TopChatCategoryBots or TopChatCategoryInlineBots":
        if q.get("@type"):
            return Object.read(q)
        return TopChatCategory()
