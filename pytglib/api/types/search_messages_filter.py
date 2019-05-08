

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
    def read(q: dict, *args) -> "SearchMessagesFilterUrl or SearchMessagesFilterDocument or SearchMessagesFilterVoiceNote or SearchMessagesFilterAudio or SearchMessagesFilterAnimation or SearchMessagesFilterCall or SearchMessagesFilterEmpty or SearchMessagesFilterUnreadMention or SearchMessagesFilterVideoNote or SearchMessagesFilterPhoto or SearchMessagesFilterChatPhoto or SearchMessagesFilterPhotoAndVideo or SearchMessagesFilterMention or SearchMessagesFilterVideo or SearchMessagesFilterVoiceAndVideoNote or SearchMessagesFilterMissedCall":
        if q.get("@type"):
            return Object.read(q)
        return SearchMessagesFilter()
