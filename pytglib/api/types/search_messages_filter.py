

from ..utils import Object


class SearchMessagesFilter(Object):
    """
    Represents a filter for message search results

    No parameters required.
    """
    ID = "searchMessagesFilter"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "SearchMessagesFilterEmpty or SearchMessagesFilterAudio or SearchMessagesFilterUrl or SearchMessagesFilterPhoto or SearchMessagesFilterMissedCall or SearchMessagesFilterVideoNote or SearchMessagesFilterVoiceAndVideoNote or SearchMessagesFilterVoiceNote or SearchMessagesFilterCall or SearchMessagesFilterMention or SearchMessagesFilterUnreadMention or SearchMessagesFilterAnimation or SearchMessagesFilterDocument or SearchMessagesFilterVideo or SearchMessagesFilterPhotoAndVideo or SearchMessagesFilterChatPhoto":
        if q.get("@type"):
            return Object.read(q)
        return SearchMessagesFilter()
