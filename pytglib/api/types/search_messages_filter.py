

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
    def read(q: dict, *args) -> "SearchMessagesFilterPhotoAndVideo or SearchMessagesFilterVoiceAndVideoNote or SearchMessagesFilterMissedCall or SearchMessagesFilterMention or SearchMessagesFilterUnreadMention or SearchMessagesFilterPhoto or SearchMessagesFilterEmpty or SearchMessagesFilterAudio or SearchMessagesFilterAnimation or SearchMessagesFilterChatPhoto or SearchMessagesFilterVideoNote or SearchMessagesFilterVoiceNote or SearchMessagesFilterUrl or SearchMessagesFilterDocument or SearchMessagesFilterCall or SearchMessagesFilterVideo":
        if q.get("@type"):
            return Object.read(q)
        return SearchMessagesFilter()
