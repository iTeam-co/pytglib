

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
    def read(q: dict, *args) -> "InlineQueryResultLocation or InlineQueryResultDocument or InlineQueryResultAnimation or InlineQueryResultContact or InlineQueryResultGame or InlineQueryResultVenue or InlineQueryResultSticker or InlineQueryResultPhoto or InlineQueryResultVoiceNote or InlineQueryResultAudio or InlineQueryResultArticle or InlineQueryResultVideo":
        if q.get("@type"):
            return Object.read(q)
        return InlineQueryResult()
