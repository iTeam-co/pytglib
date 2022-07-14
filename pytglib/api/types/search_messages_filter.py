

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
    def read(q: dict, *args) -> "SearchMessagesFilterFailedToSend or SearchMessagesFilterDocument or SearchMessagesFilterMention or SearchMessagesFilterVoiceNote or SearchMessagesFilterPinned or SearchMessagesFilterPhoto or SearchMessagesFilterUnreadMention or SearchMessagesFilterUnreadReaction or SearchMessagesFilterAudio or SearchMessagesFilterUrl or SearchMessagesFilterChatPhoto or SearchMessagesFilterAnimation or SearchMessagesFilterVideoNote or SearchMessagesFilterVideo or SearchMessagesFilterEmpty or SearchMessagesFilterPhotoAndVideo or SearchMessagesFilterVoiceAndVideoNote":
        if q.get("@type"):
            return Object.read(q)
        return SearchMessagesFilter()
