

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
    def read(q: dict, *args) -> "SearchMessagesFilterChatPhoto or SearchMessagesFilterVoiceAndVideoNote or SearchMessagesFilterCall or SearchMessagesFilterPhotoAndVideo or SearchMessagesFilterDocument or SearchMessagesFilterVideoNote or SearchMessagesFilterEmpty or SearchMessagesFilterPhoto or SearchMessagesFilterVideo or SearchMessagesFilterUrl or SearchMessagesFilterVoiceNote or SearchMessagesFilterMention or SearchMessagesFilterAnimation or SearchMessagesFilterMissedCall or SearchMessagesFilterAudio or SearchMessagesFilterUnreadMention":
        if q.get("@type"):
            return Object.read(q)
        return SearchMessagesFilter()
