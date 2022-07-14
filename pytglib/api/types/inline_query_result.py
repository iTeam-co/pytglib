

from ..utils import Object


class InlineQueryResult(Object):
    """
    Represents a single result of an inline query

    No parameters required.
    """
    ID = "inlineQueryResult"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultDocument or InlineQueryResultVenue or InlineQueryResultContact or InlineQueryResultSticker or InlineQueryResultArticle or InlineQueryResultLocation or InlineQueryResultPhoto or InlineQueryResultAnimation or InlineQueryResultVoiceNote or InlineQueryResultAudio or InlineQueryResultGame or InlineQueryResultVideo":
        if q.get("@type"):
            return Object.read(q)
        return InlineQueryResult()
