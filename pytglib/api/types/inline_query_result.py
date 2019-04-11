

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
    def read(q: dict, *args) -> "InlineQueryResultAudio or InlineQueryResultDocument or InlineQueryResultGame or InlineQueryResultContact or InlineQueryResultSticker or InlineQueryResultLocation or InlineQueryResultVideo or InlineQueryResultVoiceNote or InlineQueryResultVenue or InlineQueryResultAnimation or InlineQueryResultArticle or InlineQueryResultPhoto":
        if q.get("@type"):
            return Object.read(q)
        return InlineQueryResult()
